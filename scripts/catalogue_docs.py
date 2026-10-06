"""Render public catalogue definitions as readable Markdown, without dependencies."""

import sys
from reference import ROOT, load_json


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render():
    capabilities = load_json(ROOT / "data/technology-capabilities.json")
    questions = load_json(ROOT / "data/mdr-questions.json")
    stages = load_json(ROOT / "data/shift-map.json")
    stage_names = {s["id"]: s["title"] for s in stages["stages"] + stages["crossCutting"]}
    lines = ["# Detailed technology checks", "", "Generated from [technology-capabilities.json](../data/technology-capabilities.json). Edit the JSON definitions, then regenerate this document. Do not score everything by default: select checks relevant to your needs.", "", "IDs and source groupings preserve compatibility. Display guidance can differ from historical grouping; see [catalogue boundaries](catalogue.md).", ""]
    for zone in [s["id"] for s in stages["stages"]] + ["platform"]:
        lines += ["## " + stage_names[zone] + " (source grouping)", "", "| ID | Capability and evaluation question | Current display guidance |", "| --- | --- | --- |"]
        for c in capabilities["capabilities"]:
            if c["sourceZone"] == zone:
                lines.append("| `" + c["id"] + "` | **" + cell(c["name"]) + "**. " + cell(c["description"]) + " | " + cell(", ".join(stage_names[s] for s in c["shiftMapStages"])) + " |")
        lines.append("")
    technology = "\n".join(lines)
    lines = ["# MDR service questionnaire", "", "Generated from [mdr-questions.json](../data/mdr-questions.json). Edit the JSON definitions, then regenerate this document.", "", "Evaluate a named service package. Human delivery is not software autonomy. A section marked Roadmap only or Not offered requires only its availability declaration; optional notes remain available. See the [MDR guide](mdr.md) for interpretation.", ""]
    for section in questions["sections"]:
        lines += ["## " + section["title"], "", section["description"], ""]
        for q in questions["questions"]:
            if q["section"] != section["id"]:
                continue
            lines += ["### " + q["label"], "", "ID: `" + q["id"] + "`. " + ("Optional." if q["optional"] else "Required when this section is offered."), "", q["description"], "", "**Example:** " + q["example"], ""]
            if "options" in q:
                lines += [("Select all that apply." if q["multiple"] else "Select one."), ""]
                lines += ["- " + o["label"] + " (`" + o["value"] + "`)" for o in q["options"]]
                lines.append("")
            else:
                lines += ["Answer with text.", ""]
    return {"docs/technology-capabilities.md": technology, "docs/mdr-questionnaire.md": "\n".join(lines)}


def check():
    errors = []
    for path, expected in render().items():
        target = ROOT / path
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            errors.append(path + " is missing or out of date; regenerate it")
    return errors


if __name__ == "__main__":
    if sys.argv[1:] == ["--write"]:
        for path, content in render().items():
            (ROOT / path).write_text(content, encoding="utf-8")
            print("Updated " + path)
    else:
        errors = check()
        if errors:
            sys.exit("\n".join(errors))
        print("Readable catalogue documents are current.")
