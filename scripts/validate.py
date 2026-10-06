"""Validate public definitions, examples and local documentation links offline."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from reference import ROOT, VERSION, ZONES, EVIDENCE, TECH_DELIVERY, keys, load_json, objects, require, run, text
from catalogue_docs import check as check_rendered

META = {"schemaVersion", "frameworkVersion", "publicationRevision", "sourceRevision", "kind"}


def unique(rows, field, label):
    values = [r[field] for r in rows]
    require(all(text(v) for v in values), label + " has a blank identifier")
    require(len(values) == len(set(values)), label + " has duplicate identifiers")
    return set(values)


def strings(value, label, allowed=None):
    require(isinstance(value, list) and value and all(text(v) for v in value), label + " needs a non-empty string list")
    require(len(value) == len(set(value)), label + " contains duplicates")
    if allowed is not None:
        require(set(value) <= allowed, label + " contains unknown values")


def definitions():
    paths = sorted((ROOT / "data").glob("*.json"))
    docs = {p.stem: load_json(p) for p in paths}
    manifest = docs["manifest"]
    keys(manifest, META | {"name", "documentationUpdated", "applicationFrameworkRelease", "scoringEngine", "sourceNote", "catalogueFiles", "counts"})
    require(type(manifest["schemaVersion"]) is int and manifest["schemaVersion"] == 1, "Unsupported schema version")
    require(manifest["frameworkVersion"] == VERSION, "Reference and catalogue versions differ")
    require(re.fullmatch(r"[0-9a-f]{40}", manifest["sourceRevision"]) is not None, "Invalid source revision")
    strings(manifest["catalogueFiles"], "Catalogue files")
    require(set(manifest["catalogueFiles"]) == {p.name for p in paths if p.stem != "manifest"}, "Manifest file list differs from data directory")
    for name, doc in docs.items():
        for field in META - {"kind"}:
            require(type(doc.get(field)) is type(manifest[field]) and doc[field] == manifest[field], name + " metadata differs: " + field)
        require(doc.get("kind") == name, "Filename and kind differ: " + name)

    shift = docs["shift-map"]
    keys(shift, META | {"stages", "crossCutting"})
    stages = objects(shift["stages"], "stages")
    require([s["id"] for s in stages] == list(ZONES[:-1]), "Shift Map order changed without a schema decision")
    for stage in stages:
        keys(stage, {"id", "position", "title", "capabilities", "question", "description", "checks"})
        for field in ("position", "title", "question", "description"):
            require(text(stage[field]), "Empty stage " + field)
        strings(stage["capabilities"], "Stage capabilities")
        strings(stage["checks"], "Stage checks")
    cross = objects(shift["crossCutting"], "cross-cutting areas")
    require(unique(cross, "id", "Cross-cutting areas") == {"platform", "cross_cutting"}, "Unknown cross-cutting area")
    for row in cross:
        keys(row, {"id", "title", "description"})
        require(text(row["title"]) and text(row["description"]), "Empty cross-cutting guidance")
    placement = set(ZONES) | {"cross_cutting"}

    tech = docs["technology-capabilities"]
    keys(tech, META | {"capabilities"})
    caps = objects(tech["capabilities"], "capabilities")
    unique(caps, "id", "Capabilities")
    for c in caps:
        keys(c, {"id", "name", "description", "sourceZone", "subdomain", "scale", "shiftMapStages", "tracksIntegrations"})
        require(all(text(c[f]) for f in ("name", "description", "subdomain")), "Empty capability definition")
        require(c["sourceZone"] in ZONES, "Unknown source zone")
        require(c["scale"] == ("functional" if c["sourceZone"] == "platform" else "autonomy"), "Wrong capability scale")
        require(type(c["tracksIntegrations"]) is bool, "tracksIntegrations must be boolean")
        strings(c["shiftMapStages"], "Capability display guidance", placement)

    research = docs["research-criteria"]
    keys(research, META | {"criteria"})
    criteria = objects(research["criteria"], "criteria")
    unique(criteria, "id", "Criteria")
    for c in criteria:
        keys(c, {"id", "title", "sourceZone", "track", "shiftMapStages"})
        require(c["track"] in ("technology", "mdr") and text(c["title"]), "Invalid research criterion")
        require(c["id"].startswith("mdr." if c["track"] == "mdr" else "research."), "Wrong criterion namespace")
        require(c["sourceZone"] in ZONES, "Unknown criterion source zone")
        strings(c["shiftMapStages"], "Criterion display guidance", placement)

    vocab = docs["vocabulary"]
    vocabulary_keys = {"technologyDelivery", "serviceDelivery", "executionMechanisms", "evidenceBasis", "autonomy", "functional", "priorities"}
    keys(vocab, META | vocabulary_keys)
    for name in vocabulary_keys - {"priorities"}:
        rows = objects(vocab[name], name)
        unique(rows, "value", name)
        for row in rows:
            extra = {"points", "description"} if name == "autonomy" else {"points"} if name == "functional" else {"description"} if name == "technologyDelivery" else set()
            keys(row, {"value", "label"} | extra)
            require(text(row["label"]), "Empty vocabulary label")
            if "description" in row:
                require(text(row["description"]), "Empty vocabulary explanation")
            if "points" in row:
                require(type(row["points"]) is int and row["points"] in (0, 1, 2), "Invalid points")
    require({v["value"] for v in vocab["technologyDelivery"]} == TECH_DELIVERY, "Delivery vocabulary and calculator differ")
    require({v["value"] for v in vocab["evidenceBasis"]} == EVIDENCE, "Evidence vocabulary and calculator differ")
    require({v["value"]: v["points"] for v in vocab["autonomy"]} == {"0": 0, "1C": 1, "1G": 1, "1A": 1, "2": 2}, "Autonomy points changed")
    require({v["value"]: v["points"] for v in vocab["functional"]} == {"0": 0, "1": 1, "2": 2}, "Functional points changed")
    require(vocab["priorities"] == ["must", "nice", "explore", "out"], "Priority vocabulary changed")

    mdr = docs["mdr-questions"]
    keys(mdr, META | {"sections", "questions"})
    sections = objects(mdr["sections"], "MDR sections")
    section_ids = unique(sections, "id", "MDR sections")
    require({"mdr." + s for s in section_ids} == {c["id"] for c in criteria if c["track"] == "mdr"}, "MDR criteria and sections differ")
    for section in sections:
        keys(section, {"id", "title", "description"})
        require(text(section["title"]) and text(section["description"]), "Empty section guidance")
    questions = objects(mdr["questions"], "MDR questions")
    question_ids = unique(questions, "id", "MDR questions")
    for q in questions:
        keys(q, {"id", "label", "description", "example", "multiple", "optional", "section"}, {"options"})
        require(q["section"] in section_ids and q["id"].startswith("mdr." + q["section"] + "."), "Invalid question section")
        require(all(text(q[f]) for f in ("label", "description", "example")), "Missing question guidance")
        require(type(q["multiple"]) is bool and type(q["optional"]) is bool, "Question flags must be booleans")
        if "options" in q:
            options = objects(q["options"], "Question options")
            require(len(options) >= 2, "At least two choices required")
            unique(options, "value", q["id"])
            for option in options:
                keys(option, {"value", "label"})
                require(text(option["label"]), "Empty answer label")
        else:
            require(not q["multiple"], "Text question cannot be multi-select")
    for section in section_ids:
        availability = "mdr." + section + ".availability"
        require(availability in question_ids, "Missing section availability")
        q = next(q for q in questions if q["id"] == availability)
        require(q.get("options") == vocab["serviceDelivery"] and not q["optional"] and not q["multiple"], "MDR delivery choices differ")
    expected_counts = {"technologyCapabilities": len(caps), "technologyResearchCriteria": sum(c["track"] == "technology" for c in criteria), "mdrCriteria": len(section_ids), "mdrQuestions": len(questions)}
    require(manifest["counts"] == expected_counts, "Manifest counts are out of date")
    return expected_counts


def local_links(source, path, root=ROOT):
    errors = []
    # Code examples are not Markdown links. Remote links are deliberately not fetched.
    source = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", source, flags=re.M | re.S)
    if re.search(r"\[\[[^\]]+\]\(", source):
        errors.append(str(path.relative_to(root)) + ": invalid nested Markdown link")
    for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", source):
        destination = link.split(' "', 1)[0].strip().strip("<>")
        url = urlsplit(destination)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (path.parent / unquote(url.path)).resolve()
        if root.resolve() not in (target, *target.parents):
            errors.append(str(path.relative_to(root)) + ": link escapes repository: " + destination)
        elif not target.exists():
            errors.append(str(path.relative_to(root)) + ": missing link target: " + destination)
    return errors


def main():
    counts = definitions()
    for path in (ROOT / "examples").glob("*.json"):
        document = load_json(path)
        require(document.get("fictional") is True, "Committed examples must be explicitly fictional")
        run(document)
    errors = check_rendered()
    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            errors += local_links(path.read_text(encoding="utf-8"), path)
    require(not errors, "\n".join(errors))
    print("Validated definitions, fictional examples, generated guides and local links.")
    print(", ".join(name + "=" + str(value) for name, value in counts.items()))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        sys.exit("Validation failed: " + str(error))
