# Capability catalogue

This repository separates detailed technology checks, broader research criteria, and MDR service questions. They serve different purposes. Do not add their counts together or infer detailed scores from a broad declaration.

For readable question lists, open the [detailed technology checks](technology-capabilities.md) or [MDR questionnaire](mdr-questionnaire.md). The files below are the machine-readable definitions.

| File | Contents | How to use it |
| --- | --- | --- |
| [technology-capabilities.json](../data/technology-capabilities.json) | 111 detailed technology checks | Select the checks relevant to your own evaluation |
| [research-criteria.json](../data/research-criteria.json) | 28 technology research criteria and 7 MDR areas | Structure profiles and needs-based comparisons |
| [mdr-questions.json](../data/mdr-questions.json) | 53 questions with examples and choices | Understand service boundaries and prepare evidence |
| [vocabulary.json](../data/vocabulary.json) | Delivery, autonomy, execution and evidence values | Keep interpretations consistent |
| [shift-map.json](../data/shift-map.json) | Current stage descriptions and cross-cutting guidance | Understand where outcomes occur |
| [manifest.json](../data/manifest.json) | Baseline, publication revision and counts | Pin the version used by an assessment |

## Stable IDs and current placement

IDs are persistent identifiers, not instructions to infer placement from a prefix.

- `sourceZone` preserves the application grouping at the recorded source revision. Historical assessments and scoring still depend on it.
- `shiftMapStages` expresses current display guidance. `platform` is a cross-cutting evaluation layer; `cross_cutting` denotes feedback rather than a fifth stage.
- Some forensic collection IDs still begin with `right.` even though the current Shift Map places DFIR in Middle.
- Proactive hunting retains its older research ID but belongs in Middle. Detection engineering performed from hunt findings belongs on Left.
- Feedback is cross-cutting even when its historical ID contains `right.feedback`.
- Broad context and MDR detection areas can span stages. An area-level claim does not establish all capabilities in those stages.

The reference calculator uses `sourceZone` for compatibility with current saved scoring. It does not move scores into new groups automatically. Vendor placement remains a manual, evidence-based decision; the catalogue does not assign vendors to the map.

## Known coverage boundaries

The detailed catalogue is the current application seed set, not an exhaustive list of every question in the RFI or every guide topic. For example, the guide covers storage and retention, natural-language creation and maintenance, and correlation versus deduplication in more detail than some older atomic checks.

Keep those distinctions visible in the evaluation. Propose a new check with an independently testable definition rather than pretending a broad existing ID already covers it. New IDs require a versioned decision. Do not silently split or reinterpret existing IDs.

The existing verdict check names TP/FP/BTP. Inconclusive is not the same as benign true positive; assess and document that distinction explicitly when it matters. A future catalogue refinement should not overwrite the historical meaning.

## Data contract

Each catalogue includes `schemaVersion`, `frameworkVersion`, `publicationRevision`, and `sourceRevision`. `schemaVersion: 1` describes this public data format, not the platform's database schema or RFI payload.

Technology checks include `id`, `name`, `description`, `sourceZone`, `subdomain`, `scale`, `shiftMapStages` and `tracksIntegrations`. Research criteria have a `track` and use their own namespace. MDR questions have stable field IDs, section IDs, descriptions, examples, optionality and choices.

For an MDR section declared `roadmap` or `not_supported`, the current RFI only requires its availability declaration; optional notes remain available. In other sections, required questions follow the listed types and choices. A multiple-choice “none” answer must not coexist with positive choices.

These files contain definitions only. They contain no completed vendor answers, analyst findings, customer evidence, account IDs or publication permissions.

## Reuse and integration

Pin a commit or release rather than fetching mutable `main` during a live assessment. Preserve IDs and version metadata when exporting. Validate JSON and references with `python3 scripts/validate.py`.

There is no automatic platform synchronization or supported import endpoint in this repository. Changing a JSON file here does not change the hosted RFI. [Maintenance policy](maintenance.md).
