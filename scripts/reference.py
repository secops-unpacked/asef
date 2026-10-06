"""Offline reference calculations for the public ASEF format (not an app importer)."""

import json
import sys
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.1.3"
ZONES = ("far_left", "left", "middle", "right", "platform")
TECH_DELIVERY = {
    "not_supported", "public_roadmap", "private_preview", "public_preview",
    "ga_partner", "ga_requires_build", "ga_configured", "ga_out_of_box",
}
GA = {v for v in TECH_DELIVERY if v.startswith("ga_")}
REVIEWED = {"documentation", "demonstrated", "validated"}
EVIDENCE = REVIEWED | {"vendor_claim"}
POINTS = {"0": 0, "1C": 1, "1G": 1, "1A": 1, "1": 1, "2": 2}


def load_json(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON property: " + key)
            result[key] = value
        return result
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=unique_keys)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def objects(value, name):
    require(isinstance(value, list) and all(isinstance(v, dict) for v in value), name + " must be a list of objects")
    return value


def keys(obj, required, optional=()):
    require(isinstance(obj, dict), "Expected an object")
    require(set(required) <= set(obj), "Missing required properties: " + str(set(required) - set(obj)))
    require(set(obj) <= set(required) | set(optional), "Unexpected properties: " + str(set(obj) - set(required) - set(optional)))


def percent(count, total):
    if not total:
        return 0.0
    return float((Decimal(count) * 100 / Decimal(total)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def catalogue():
    data = load_json(ROOT / "data/technology-capabilities.json")
    return {c["id"]: c for c in data["capabilities"]}


def validate_technology(document, capabilities):
    keys(document, {"schemaVersion", "frameworkVersion", "kind", "fictional", "offering", "track", "capabilityIds", "assessments"})
    require(type(document["schemaVersion"]) is int and document["schemaVersion"] == 1, "Use public schemaVersion 1")
    require(document["frameworkVersion"] == VERSION, "Unsupported framework version; do not silently rescore historical work")
    require(document["kind"] == "technology-evaluation" and document["track"] == "technology", "Technology scoring must not be applied to MDR")
    require(type(document["fictional"]) is bool and text(document["offering"]), "Provide offering and fictional metadata")
    ids = document["capabilityIds"]
    require(isinstance(ids, list) and all(text(v) for v in ids), "capabilityIds must be a list of strings")
    require(len(set(ids)) == len(ids), "Duplicate in-scope capability")
    require(all(v in capabilities for v in ids), "Unknown capability ID")
    seen = set()
    for row in objects(document["assessments"], "assessments"):
        keys(row, {"capabilityId", "availability", "evaluator"}, {"evidenceBasis", "evidenceReference", "notes"})
        cid = row["capabilityId"]
        require(text(cid) and cid in ids and cid not in seen, "Assessment must reference a unique in-scope capability")
        seen.add(cid)
        require(row["availability"] is None or (isinstance(row["availability"], str) and row["availability"] in TECH_DELIVERY), "Invalid technology delivery")
        allowed = {"0", "1", "2"} if capabilities[cid]["scale"] == "functional" else {"0", "1C", "1G", "1A", "2"}
        require(row["evaluator"] is None or (isinstance(row["evaluator"], str) and row["evaluator"] in allowed), "Invalid rating for this scale; codes must be strings")
        if "evidenceBasis" in row:
            require(isinstance(row["evidenceBasis"], str) and row["evidenceBasis"] in EVIDENCE, "Invalid evidence basis")
        for field in ("evidenceReference", "notes"):
            if field in row:
                require(isinstance(row[field], str), field + " must be text")


def current_rating(row):
    if row is None:
        return None
    if row["availability"] == "not_supported":
        return "0"
    # Matches current ASEF 3 compatibility handling. Missing delivery is NOT GA.
    if row["availability"] is None or row["availability"] in GA:
        return row["evaluator"]
    return None


def summarize(ids, capabilities, assessments):
    ratings = [current_rating(assessments.get(cid)) for cid in ids]
    recorded = [r for r in ratings if r is not None]
    covered = sum(
        assessments.get(cid, {}).get("availability") in GA
        and (capabilities[cid]["scale"] != "functional" or POINTS.get(current_rating(assessments.get(cid)), 0) > 0)
        for cid in ids
    )
    lifecycle = [cid for cid in ids if capabilities[cid]["scale"] == "autonomy"]
    points = sum(POINTS[r] for r in recorded)
    return {
        "inScope": len(ids), "rated": len(recorded), "points": points,
        "ratedDepthPct": percent(points, 2 * len(recorded)) if recorded else None,
        "gaCoverageCount": covered, "gaCoveragePct": percent(covered, len(ids)),
        "fullAutomationPct": percent(sum(current_rating(assessments.get(cid)) == "2" for cid in lifecycle), len(lifecycle)) if lifecycle else None,
        "levelCounts": dict(sorted(Counter(recorded).items())),
        "deliveryCounts": dict(sorted(Counter(assessments.get(cid, {}).get("availability") or "unknown" for cid in ids).items())),
    }


def technology_scores(document, capabilities=None):
    capabilities = catalogue() if capabilities is None else capabilities
    validate_technology(document, capabilities)
    ids = document["capabilityIds"]
    rows = {a["capabilityId"]: a for a in document["assessments"]}
    zones = {zone: summarize([cid for cid in ids if capabilities[cid]["sourceZone"] == zone], capabilities, rows) for zone in ZONES}
    platform_score = zones["platform"]["ratedDepthPct"]
    return {
        "kind": "technology-summary", "frameworkVersion": VERSION,
        "offering": document["offering"], "fictional": document["fictional"],
        "overall": summarize(ids, capabilities, rows), "zones": zones,
        "platformWarning": platform_score is not None and platform_score < 50,
        "unconfirmedDeliveryRatings": [cid for cid, row in rows.items() if row["availability"] is None and row["evaluator"] is not None],
        "interpretation": "Descriptive capability measures, not evidence-validated effectiveness, a universal ranking, or a needs-fit score. Source zones preserve application compatibility.",
    }


def validate_comparison(document):
    keys(document, {"schemaVersion", "frameworkVersion", "kind", "fictional", "needsId", "track", "criteria", "offerings"})
    require(type(document["schemaVersion"]) is int and document["schemaVersion"] == 1 and document["frameworkVersion"] == VERSION, "Unsupported version")
    require(document["kind"] == "needs-comparison" and type(document["fictional"]) is bool and text(document["needsId"]), "Invalid comparison metadata")
    require(document["track"] in ("technology", "mdr"), "Compare one offering track at a time")
    all_criteria = load_json(ROOT / "data/research-criteria.json")["criteria"]
    known = {c["id"]: c["track"] for c in all_criteria}
    known.update({cid: "technology" for cid in catalogue()})
    seen = set()
    for c in objects(document["criteria"], "criteria"):
        keys(c, {"id", "priority", "successCriterion"})
        require(text(c["id"]) and known.get(c["id"]) == document["track"] and c["id"] not in seen, "Criterion must be unique and belong to the selected track")
        seen.add(c["id"])
        require(c["priority"] in ("must", "nice", "explore", "out") and text(c["successCriterion"]), "Specify priority and success criterion")
    profiles = set()
    for offering in objects(document["offerings"], "offerings"):
        keys(offering, {"id", "name", "revision", "track", "reviewContext", "findings"})
        require(text(offering["id"]) and text(offering["name"]) and offering["id"] not in profiles, "Offering IDs must be unique")
        profiles.add(offering["id"])
        require(type(offering["revision"]) is int and offering["revision"] > 0 and offering["track"] == document["track"], "Offering revision or track mismatch")
        ctx = offering["reviewContext"]
        if ctx is not None:
            keys(ctx, {"needsId", "profileId", "profileRevision", "track"})
            require(text(ctx["needsId"]) and text(ctx["profileId"]) and type(ctx["profileRevision"]) is int and ctx["profileRevision"] > 0 and ctx["track"] in ("technology", "mdr"), "Invalid review context")
        seen_findings = set()
        for f in objects(offering["findings"], "findings"):
            keys(f, {"criterionId", "outcomeCriterion", "outcome", "evidenceBasis", "evidenceReference"})
            require(text(f["criterionId"]) and f["criterionId"] in seen and f["criterionId"] not in seen_findings, "Findings must reference unique selected criteria")
            seen_findings.add(f["criterionId"])
            require(f["outcome"] is None or (type(f["outcome"]) is int and f["outcome"] in (0, 1, 2)), "Outcome must be null, 0, 1 or 2")
            require(text(f["outcomeCriterion"]) and isinstance(f["evidenceReference"], str), "Finding criterion and evidence reference must be text")
            require(isinstance(f["evidenceBasis"], str) and f["evidenceBasis"] in EVIDENCE, "Invalid evidence basis")


def needs_comparison(document):
    validate_comparison(document)
    required = [c for c in document["criteria"] if c["priority"] == "must"]
    result = []
    for offering in document["offerings"]:
        context = {"needsId": document["needsId"], "profileId": offering["id"], "profileRevision": offering["revision"], "track": document["track"]}
        current = offering["reviewContext"] == context
        findings = {f["criterionId"]: f for f in offering["findings"]} if current else {}
        counts = {"met": 0, "partial": 0, "unmet": 0, "unknown": 0}
        for criterion in required:
            f = findings.get(criterion["id"])
            reviewed = f and f["outcomeCriterion"] == criterion["successCriterion"] and f["evidenceBasis"] in REVIEWED and text(f["evidenceReference"])
            outcome = f["outcome"] if reviewed else None
            counts[{0: "unmet", 1: "partial", 2: "met"}.get(outcome, "unknown")] += 1
        result.append({"offering": offering["name"], "mustHaves": len(required), **counts, "stale": offering["reviewContext"] is not None and not current})
    return {"kind": "needs-fit-summary", "track": document["track"], "fictional": document["fictional"], "offerings": result,
            "interpretation": "Reviewed must-have outcomes only. Evidence quality must be assessed by a person; supplying a reference is not automatic verification."}


def run(document):
    require(isinstance(document, dict), "Input must be an object")
    if document.get("kind") == "technology-evaluation":
        return technology_scores(document)
    if document.get("kind") == "needs-comparison":
        return needs_comparison(document)
    raise ValueError("Choose technology-evaluation or needs-comparison. Platform backups are not supported.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scripts/reference.py path/to/public-format.json")
    try:
        print(json.dumps(run(load_json(sys.argv[1])), indent=2))
    except (ValueError, TypeError, KeyError, OSError) as error:
        sys.exit("Invalid evaluation: " + str(error))
