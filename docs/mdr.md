# Evaluating an MDR service

The unit of evaluation is the **named service package and contracted operating boundary**, not every feature in the provider's internal stack.

Ask what the customer's team receives, who does the work, and how the result is verified. AI usage is one dimension, not the purpose of the score.

## What to examine

| Area | Practical checks |
| --- | --- |
| Sources and intake | Customer SIEM or data lake, direct detection tools, raw telemetry, employee reports, custom SOC requests, connector ownership |
| Detection and hunting | Who develops detections, customer visibility and edit/export rights, proactive and reactive hunts, threat-intelligence-led campaigns and follow-up |
| Enrichment and context | Security history and business context, graph/database/retrieval architecture, freshness, corrections, historical imports and retrospective searches |
| Investigation and DFIR | Triage, timeline, blast radius, employee interaction, forensic collection versus full DFIR, evidence integrity and chain of custody |
| Remediation and handover | Actions actually executed, customer processes, approvals, verification, escalation ownership, recovery and where responsibility ends |
| Feedback | Corrections, reopened cases, review of automatically closed cases, implemented changes and customer-visible validation |
| Service transparency and trust | Per-step attribution, safe fallback, permissions, auditability, data boundaries, service hours and commitments |

Hunting and DFIR belong in Middle on the current Shift Map. Detection changes belong on Left. Feedback applies across stages.

## Separate three questions

1. **Is it in the package?** Included, paid add-on, named partner, roadmap or not offered.
2. **Who performs it?** Provider analysts, deterministic automation, ML, LLM/agent reasoning, or a combination.
3. **Who authorizes it?** Customer authorization and provider-human oversight are different controls.

For example, a customer may pre-authorize endpoint containment while a provider analyst still approves every execution. That is not unattended product autonomy.

## Follow one case end to end

Start at intake and trace the case through enrichment, investigation, action, verification and closure. Identify human and automated steps, what the customer had to do, and one resulting improvement. Ask for a redacted timeline with evidence, approvals and exceptions.

Human delivery is valid. A deterministic integration can be the right choice. A graph does not automatically improve an outcome, and adding an LLM does not establish autonomous investigation.

## Compare like for like

Use the same source requirements, coverage hours, authorization boundaries and success criteria. Record exclusions and add-ons rather than treating the broad provider portfolio as included.

There is no validated universal MDR autonomy score here. Use evidence-backed Met, Partially met, Unmet and Unknown findings against the buyer's needs. Do not convert analyst-delivered work into software autonomy points.

If a provider also sells customer-operated software, evaluate that named product in the technology track and retain a separate service comparison.

[All MDR questions and examples](mdr-questionnaire.md) · [Full methodology](methodology.md)
