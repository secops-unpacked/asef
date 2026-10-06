# ASEF: AI SecOps Evaluation Framework

**Evaluate what a vendor delivers for your team, not how it markets itself.**

ASEF is a practitioner-led framework from [SecOps Unpacked](https://secops-unpacked.ai/asef/guide) for evaluating AI-enabled technology and MDR services across the full SecOps lifecycle. AI SOC evaluation is part of that scope, not its boundary.

Start with your needs. Understand the offering. Compare against the same requirements. Verify what matters.

This is the public methodology and contribution repository. It is **not** the source code for the SecOps Unpacked platform, a vendor leaderboard, or a collection of vendor submissions.

## Use ASEF online

**[Open the interactive ASEF framework on SecOps Unpacked](https://secops-unpacked.ai/asef/guide)**

Use the website to define your needs, explore available vendor profiles, compare offerings and run your own evaluations. Use this repository to read the methodology and contribute improvements. Repository changes do not automatically update the live platform.

## Start here

| What you want to do | Where to go |
| --- | --- |
| Understand ASEF in a few minutes | [Practical guide](docs/guide.md) |
| Read the full evaluation methodology | [Framework reference](docs/methodology.md) |
| See exactly what can be evaluated | [Capability catalogue](docs/catalogue.md) |
| Evaluate an MDR service | [MDR guide](docs/mdr.md) |
| Understand the calculations | [Scoring and worked examples](docs/scoring.md) |
| Use the online evaluation tools | [Open ASEF](https://secops-unpacked.ai/asef/guide) |
| Suggest a correction or missing capability | [Submit a contribution](https://github.com/secops-unpacked/asef/issues/new/choose) |
| Discuss a methodology question | [Discussions](https://github.com/secops-unpacked/asef/discussions) |

No coding is needed to suggest an improvement. An explanation of what is unclear, why it matters, and a practical example is enough.

## Four ways to use ASEF

1. **Find potential vendors:** describe your environment, needs and constraints.
2. **Understand a platform or service:** read an available technical profile without creating a score.
3. **Compare a known shortlist:** compare offerings against the same must-haves and success criteria.
4. **Run your own PoC:** test selected capabilities, record evidence and assign your own findings.

Technology and MDR are separate tracks. A company can be evaluated on both, but its service and software should not receive one blended score.

## The SecOps Shift Map

| Far Left | Left | Middle | Right |
| --- | --- | --- | --- |
| **Data foundation** | **Detection and readiness** | **Investigation and understanding** | **Remediation and improvements** |
| Pipelines, ingestion, processing, retention | Detection engines, engineering, validation, resilience, context DBs and graphs | Triage, investigation, DFIR, proactive and reactive threat hunting | Mitigation, remediation, verification and recovery |

**Platform and Trust** applies across the offering. **Feedback** is cross-cutting: it can improve any stage and does not, by itself, establish remediation capability. Building context belongs on Left; using it in investigation belongs in Middle.

Position on the map is not a maturity rank, quality score, or autonomy level.

## What stays separate

- **Delivery:** shipped out of the box, configurable, customer-built, partner-delivered, preview, roadmap or unsupported.
- **Autonomy:** manual, assisted, approval before action, intervention after action, or end-to-end execution.
- **Execution:** human work, deterministic automation, ML, LLM/agents, or a combination.
- **Evidence:** a vendor claim, reviewed documentation, an observed demonstration or validation in your environment.
- **Fit:** whether reviewed evidence meets your specific requirement.

More autonomy does not automatically mean a better fit. Unknown is not the same as unsupported. General availability is not proof of effectiveness. ROI and post-implementation financial measurement are outside this framework.

## What is in this repository

- 111 detailed technology checks, 28 technology research criteria and 7 MDR comparison areas.
- 53 MDR questions, including descriptions, examples and answer choices.
- Machine-readable JSON with stable IDs and a versioned vocabulary.
- Fictional examples and a small, dependency-free reference calculator.
- Contribution forms, review rules, attribution and change history.

These are different levels of detail, **not additive coverage scores**. A broad research claim must not automatically populate every detailed capability. The catalogue is a baseline, not an exhaustive statement that every current guide topic has a dedicated scored check. See [catalogue boundaries](docs/catalogue.md).

## Current publication

Framework baseline: **3.1.3**. Public documentation revision: **2026-10-06.1**.

This initial publication follows the October 6 documentation alignment. It does not deploy changes to the application or rewrite historical evaluations. [Version and synchronization policy](docs/maintenance.md).

As of October 6, 2026, SecOps Unpacked is conducting in-depth research on around 40 vendors. Full technical profiles are planned for November 2026, subject to review and vendor approval. Check the platform for current availability; private submissions are not published here.

## Run the reference checks

Python 3.9 or later. No dependencies, account, API key or database needed.

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/reference.py examples/technology-evaluation.json
python3 scripts/reference.py examples/needs-comparison.json
```

The calculator is an illustrative reference for the documented calculations, not a platform backup importer or a complete replacement for the hosted application.

## Contribute and reuse

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Vendors are welcome to contribute, with relevant affiliations disclosed. Contributions do not confer endorsement or favorable evaluation.

Published under **[CC BY 4.0](LICENSE)**. Commercial reuse and adaptations are permitted under the license, with attribution and changes identified. See [NOTICE.md](NOTICE.md) for attribution and scope. The license does not grant trademark rights or imply endorsement.

Created by Filip Stojkovski / SecOps Unpacked, with [contributors and acknowledgements](CONTRIBUTORS.md).
