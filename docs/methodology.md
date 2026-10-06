# ASEF: AI SecOps Evaluation Framework

> Framework v3.1.3. Documentation updated October 6, 2026. [Start with the quick guide](guide.md).

This reference describes evaluation, not post-implementation financial measurement. The public repository does not run the hosted application.

## 1. Overview

ASEF, the AI SecOps Evaluation Framework, helps practitioners identify relevant vendors, understand what they deliver, compare alternatives against the same requirements, and run their own proof of concept. It covers AI SOC evaluation as part of the wider SecOps lifecycle, not as the boundary of the framework.

Start with the work your team needs done, your existing stack, operating model, and constraints. The output is an explainable evaluation of fit, strengths, gaps, delivery dependencies and evidence. It is not a universal best-vendor ranking. Vendors can use the same framework to understand what practitioners will examine.

ASEF is an evaluation framework. It separates discovery signals, vendor-declared capabilities, reviewed evidence and practitioner findings. Post-implementation operations tracking is outside this document's scope. A short briefing, a published profile and a customer PoC provide different kinds of information and must not be treated as interchangeable.

### Relationship to ARMM

ASEF draws on ARMM, the [AI Response Maturity Model](https://armm.secops-unpacked.ai/), for its action catalogue and human-involvement vocabulary, and extends evaluation across the full SecOps lifecycle. Current ASEF no longer uses Builder mode, Trust/Complexity/Impact sums, or Explorer-to-Expert tiers to rank products. Historical evaluation data is preserved, but it is not the current methodology.

## 2. Four ways to use ASEF

Choose the starting point that fits your task. You do not need to complete a single mandatory funnel. Define needs to discover potential vendors, read a technical profile without scoring, compare a known shortlist, or run your own PoC. Platform and Trust remains relevant whichever path you choose.

| Starting point | What you do |
| --- | --- |
| Find vendors | Describe your environment, current tools, target outcomes and constraints in Needs. Review suggested vendors and the facts that still need verification. |
| Understand a platform | Open a vendor profile. Where a published technical profile is available, read its capabilities, delivery model and autonomy without creating an evaluation. |
| Compare a shortlist | Select published offerings and a saved needs profile. Compare technology with technology or MDR with MDR against the same must-haves and success criteria. |
| Run your own PoC | Choose vendors, link requirements, test relevant capabilities, record evidence and assign your own scores. Compare saved evaluations using the same scope. |
| Make a decision | Read capability fit, delivery effort, autonomy, trust and unresolved gaps together. A suggestion or vendor declaration is not a validated outcome. |

## 3. The SecOps Shift Map

The Shift Map shows where a product or service contributes to the SecOps lifecycle. Four stages run left to right. Platform and Trust is a cross-cutting evaluation layer, not a fifth lifecycle stage. Position is not a maturity ladder, quality score or autonomy level.

| Stage | Assessment | Role | Focus |
| --- | --- | --- | --- |
| Far Left: Data foundation | Delivery + autonomy | Lifecycle | Pipelines, ingestion, processing, retention |
| Left: Detection and readiness | Delivery + autonomy | Lifecycle | Detection, validation, resilience, context |
| Middle: Investigation and understanding | Delivery + autonomy | Lifecycle | Triage, investigation, DFIR, hunting |
| Right: Remediation and improvements | Delivery + autonomy | Lifecycle | Mitigation and remediation |
| Platform and Trust | Functional support | Cross-cutting | Operations, security and governance |

Feedback is explained separately as cross-cutting: capture outcomes, review them and verify what changes. It can improve data, detections, investigations or remediation through people, automation or AI. Feedback alone does not establish Right-stage coverage or autonomous remediation. Building and maintaining context belongs on Left; using that context in enrichment and investigation belongs in Middle.

## 4. Capabilities and offering tracks

Keep three levels distinct: directory categories help discovery; Shift Map stages describe where work happens; evaluation criteria define what to inspect. A category tag or broad RFI answer does not prove every detailed capability underneath it. The current catalogue is versioned, and saved capability IDs remain stable.

| Area | What to examine |
| --- | --- |
| Data foundation | Source onboarding; shipped versus custom connectors; parsing and normalization; schema mapping; quality and coverage; routing and filtering; pipeline health; storage, retention, retrieval and deletion. |
| Detection and readiness | Detection engines versus rules for another engine; authoring, tuning and deployment; coverage validation and attack simulation; resilience; context collection, storage, relationships, freshness and provenance. |
| Investigation and understanding | Enrichment sources and customer control; correlation and deduplication as separate checks; upstream SIEM dependencies; investigation depth, timelines and blast radius; verdicts; proactive and reactive hunting; DFIR and evidence integrity. |
| Remediation and improvements | Mitigation and remediation across identity, network, endpoint, cloud and SaaS; shipped actions versus customer-built workflows; approvals; customer procedures; execution verification and recovery from failed actions. |
| Platform and Trust | Deployment, integrations and write-back; identity and access; auditability; data handling; model controls; reliability; governance; natural-language creation and maintenance where relevant. |

DFIR belongs with investigation and understanding. Assess collection, analysis, timelines, root cause, evidence integrity and chain of custody, and distinguish them from actions intended to contain or remediate a threat. Existing action IDs and saved RFI groupings are retained for compatibility; their historical location does not redefine the current public Shift Map.

Threat hunting includes proactive hypothesis- or threat-intelligence-led hunts and reactive hunts triggered by an incident. Assess initiation, supported tools and data sources, campaign tracking and follow-up. Hunting sits in Middle; creating or improving detections from hunt findings contributes to Left. Do not infer detection engineering merely because hunting is offered.

### Two offering tracks: technology and MDR

Technology evaluates a named product the customer can operate: what is shipped, what must be configured or built, its autonomy and execution mechanism, and its platform controls. Record natural-language creation and maintenance separately for workflows, integrations, dashboards and agents. Investigate how context is gathered and stored, including security history and business context; a graph is an architecture choice, not an automatic quality score.

MDR evaluates the named service and package the customer receives. Examine intake from the existing SIEM, detection tools, telemetry and employee requests; enrichment and organizational context; customer-visible detection engineering; proactive and reactive hunting; investigation and DFIR; employee interaction; mitigation, remediation, escalation and handover boundaries; and implemented feedback. Identify included service, paid add-on, named-partner delivery, roadmap and not-offered items.

For MDR, distinguish provider human analysts, deterministic automation, ML and LLM or agent reasoning. Record approval-before-action, supervision or veto, and customer-specific procedures. Explain what the provider owns, what remains with the customer, and how completed work and improvements are visible. Internal service tooling is not automatically a customer-available software product. A vendor offering both tracks receives separate comparisons, not a blended technology-plus-service score.

## 5. Delivery, autonomy and evidence

Record delivery, autonomy and evidence separately. Availability tells you whether a capability exists and what is needed to use it. Autonomy tells you how independently the system operates. Evidence tells you what supports the assessment. Higher autonomy is not automatically better for the buyer.

### Autonomy scale for technology capabilities

| Code | Label | Meaning | Points |
| --- | --- | --- | --- |
| 0 | Manual | The person performs the work. No autonomy; delivery records whether the capability exists. | 0 |
| 1C | Collaborator | The system assists; the human performs the action. | 1 |
| 1G | Guide | The system proposes; the human approves before execution. | 1 |
| 1A | Approver | The system acts within policy; a human can veto or intervene. | 1 |
| 2 | Automated | Runs end to end without case-by-case human involvement. | 2 |

Do not confuse approval with veto: 1G requires approval before execution; 1A permits execution with human intervention. Level 0 is manual, not missing. Autonomy may use deterministic automation, ML, LLM or agent reasoning, or a combination. Record the mechanism and operating boundaries rather than treating autonomy as an LLM-only score.

### Function scale (Platform and Trust)

| Code | Label | Meaning | Points |
| --- | --- | --- | --- |
| 0 | None | No functional support. | 0 |
| 1 | Limited | Present, but only partially supports the requirement. | 1 |
| 2 | Full | Fully supports the assessed requirement. | 2 |

### Unknown, not supported and out of scope

Unknown means information or assessment is missing. Not supported records a known capability gap. Out of scope means the buyer has deliberately excluded a capability from this evaluation and its denominator. Manual is a valid delivery mode, not an exclusion. Do not mark a must-have out of scope simply because the vendor lacks it.

### Delivery and evidence, replacing Builder mode

For technology, use the shared RFI delivery vocabulary: GA out of the box; GA with configuration; GA, customer build required; GA via a required partner or managed service; public preview; private preview; public roadmap; or not supported. GA means generally available, not independently verified.

| Dimension | Question it answers |
| --- | --- |
| Delivery | What ships today, and who must configure, build or operate it? |
| Autonomy | Who performs, approves or supervises the work, and by what mechanism? |
| Evidence | Is this a vendor claim, reviewed documentation, observed demo or environment validation? |

Out of the box means a pre-built capability after standard onboarding. Configuration means setup or tuning without building a new workflow, agent or connector. Customer build means creating and maintaining those components. Required partner delivery is not native product functionality. Record evidence basis and a relevant reference; a published RFI remains a vendor claim unless separately reviewed or tested.

## 6. How evaluation results are calculated

ASEF 3 reports a capability profile rather than a blended maturity ranking. Keep delivery, coverage, autonomy, evidence and requirement fit visible separately. The practitioner capability evaluation and published-profile needs comparison have different calculations; neither turns a vendor claim into a verified outcome.

### Per-zone and subdomain measures

Rated-depth percentage = recorded points / (2 × rated capabilities) × 100. Manual scores 0 points; 1C, 1G and 1A each score 1; level 2 scores 2. Platform uses None = 0, Limited = 1 and Full = 2. Unrated checks are excluded from this percentage, so always show the rated count. No ratings means no depth result, not failure.

Current GA coverage = in-scope capabilities with recorded generally available delivery / in-scope capabilities × 100. For lifecycle capabilities, manual GA delivery counts as present. For Platform and Trust, recorded GA delivery must also have a positive functional rating. Unknown, unsupported, preview and roadmap entries do not count as covered.

Full automation is the proportion of in-scope lifecycle capabilities rated level 2 under the selected scoring engine. It is not a quality or effectiveness score. Preview and roadmap ratings do not contribute to current ASEF 3 scoring.

Autonomy distribution shows the counts and shares of rated capabilities at 0, 1C, 1G, 1A and 2. Read these alongside delivery and evidence. A manual GA capability can be covered while contributing zero autonomy points.

Customer effort stays visible through delivery categories. GA coverage includes customer-build and required-partner paths, so it must never be presented as out-of-the-box coverage. Two products with the same coverage percentage may require very different implementation work.

Subdomain detail exposes gaps that a zone summary can hide. Use the same scope and capability set for comparisons, and show assessed versus in-scope counts beside percentages. Availability, evidence and autonomy are different dimensions; a high depth percentage based on a few ratings does not establish broad coverage.

### Three outputs that must not be conflated

Discovery suggests potential fit. Published profiles describe an offering. Practitioner findings assess it against the buyer's requirements. Keep those outputs separate rather than collapsing them into one leaderboard.

| Output | How to read it |
| --- | --- |
| Vendor suggestion | A potential match based on published categories, scope and available facts. It is not an endorsement or capability score. |
| Capability profile | Delivery, coverage, autonomy, evidence and Platform and Trust by area. Broad declarations do not automatically fill detailed capability ratings. |
| Needs-fit findings | Private, evidence-referenced findings against the buyer's must-haves: met, partially met, unmet or unknown. |

### Needs-fit comparison

The comparison summary counts must-have criteria as met, partial, gaps or unknown. Nice-to-have and Explore priorities remain useful context but do not enter the must-have tally. A reviewed outcome needs a recorded result and an evidence reference backed by documentation, a demonstration or environment validation. A vendor claim alone remains unknown.

### Full scope versus focused scope

Select the lifecycle stages and capabilities relevant to the decision. Platform and Trust remains cross-cutting. Compare the same offering type and scope so one vendor is not assessed against a broader requirement set than another.

Full scope includes all four lifecycle stages. It provides a wider profile, not a universal maturity score or a requirement to buy one platform that does everything.

Focused scope includes only the work you need, such as triage and investigation. Capabilities outside that scope are excluded rather than counted as vendor weaknesses. A specialist can be a strong fit for a focused requirement.

There is no current Builder-derived program score, Full/Heavy composite or Explorer-to-Expert product tier. Zone-level detail, delivery dependencies and buyer-defined outcomes are the basis for interpretation. More autonomy and broader coverage are not substitutes for meeting a must-have.

Platform and Trust is reported separately. In the current capability evaluation, a functional percentage below 50% raises a warning; unassessed checks remain unrated. Read the warning with the assessment count and individual controls. Strong lifecycle capability cannot establish that an unverified security requirement is met.

## 7. Needs, discovery and screening

The Needs workflow captures your environment, operating model, existing tools, target outcomes, preferred autonomy and constraints. For each existing tool, state whether to keep, augment or replace it. Suggestions narrow the research space; they do not replace technical verification.

### Scope and capability priorities

Select relevant outcomes and lifecycle stages, then refine the capabilities vendors should deliver. Priorities are Must-have, Nice-to-have, Explore and Out of scope. Add a concrete success criterion where useful. Choose Technology or MDR for the comparison; settings for the other track are retained.

### Operating constraints

Record deployment preferences, required integrations, governance requirements and customer engineering capacity. A declared preference is not evidence that a vendor meets it. Use the per-capability autonomy sliders to express desired independence, and retain any separate requirement for human approval of remediation actions.

| Requirement | Buyer specifies | Evaluation treatment |
| --- | --- | --- |
| Offering and scope | Technology or MDR; lifecycle work and must-have outcomes | Compare like-for-like offerings. Category and zone matches support discovery, not proof. |
| Delivery effort | Low, moderate or high engineering capacity; acceptable build dependencies | Inspect pre-built, configured, customer-built and partner-delivered capability separately. |
| Hosting and controls | Deployment, integrations, access, governance and model requirements | Use known facts for screening; retain missing or untested support as a verification task. |

Known hard constraints can exclude a vendor. Required role-based access and bring-your-own-model support can be screening gates when selected and supported by facts. Other governance controls and required integrations may remain explicit verification items. Do not assume the platform has automatically validated every requirement.

### Screening states

The screening layer distinguishes known matches, missing facts and known conflicts. These states describe the available information, not the quality of the product.

| State | Meaning | Behavior |
| --- | --- | --- |
| Passes | Recorded facts satisfy the selected screening gates. | Eligible for the shortlist; technical claims still need checking. |
| Unknown | A required fact is missing or cannot be confirmed. | Flag for verification. Do not interpret missing information as supported or unsupported. |
| Excluded | A recorded fact conflicts with a hard requirement. | Excluded from suggestions. Review the conflicting fact before changing the requirement or considering an exception. |

A known conflict takes precedence over unknown information. An excluded vendor is not the same as an unverified one. Changing a requirement is a buyer decision, not something the matching system should silently do.

### Where suggestions and profiles come from

Suggestions use directory information, recorded Shift Map placements, deployment facts and category matches. Core categories distinguish AI SOC as Capabilities, AI SOC Pure Play and AI SOC Supporting Capability. Capability groups cover Data platforms, Detection sources, Context, Investigation and response, SecOps Engineering, and Testing and verification.

Category names and aliases evolve, for example Data Pipeline and Insider Risk. These discovery groups do not assign capability scores or automatically move vendors on the public Shift Map. Suggestions, including AI-assisted explanations where available, are hypotheses to verify. Missing detailed profiles are not evidence that a vendor lacks a capability.

### From shortlist to evaluation

Open a profile to understand the offering, compare available published profiles against saved needs, or create a practitioner evaluation. If no technical profile is published, use your own evaluation rather than filling gaps with assumptions. The saved needs profile keeps scope and constraints connected to the decision.

## 8. Platform and Trust

Platform and Trust covers deployment, operations, reliability, access control, auditability, data handling, model controls and governance. It uses functional support rather than autonomy. Evaluate these controls for the selected offering and deployment, not as generic claims about the vendor's entire portfolio.

Make each check concrete. SIEM alert bidirectional updates means examining what can be read and written, whether changes synchronize both ways, and any limitations; closing an alert alone does not prove full two-way support. Record shipped, preview, roadmap and unavailable status, and distinguish setup from new customer development. Deployment context helps interpret applicability, but it is not permission to waive a buyer's required control.

## 9. Comparisons, publication and saved work

A published technical profile is an adapted, vendor-approved view of research declarations, not a raw RFI dump or a pre-awarded practitioner score. Needs-fit findings stay separate from that source profile. Use the following outcome states only against the buyer's specific criterion:

| Outcome | Meaning |
| --- | --- |
| Unknown | Not assessed, insufficient evidence, or evidence no longer tied to the current criterion and profile revision. |
| Unmet (0) | Reviewed evidence shows the stated requirement is not met. |
| Partially met (1) | Reviewed evidence shows only part of the stated requirement is met; record the gap. |
| Met (2) | Reviewed evidence supports the stated requirement within the recorded scope and conditions. |

### From RFI to a published technical profile

A vendor can select Technology only, MDR only, or Both in the research RFI. Analysts adapt the submitted answers into the relevant technical or service profile rather than copying every briefing question one-to-one. A broad subdomain claim must not be expanded into detailed capability support without evidence.

Before publication, the vendor previews the exact profile revision, can request changes, and explicitly approves that version and its publication scope. Admin publication requires the relevant consent and approval. Material edits require fresh review and approval; consent withdrawal removes the published profile. Raw RFI responses, confidential evidence and private practitioner findings are not made public by this process.

Comparison findings are linked to the saved needs profile and the published offering's ID, track and revision. If the source revision or success criterion changes, reassess the finding instead of carrying it forward as current proof. A finding also needs a reviewed evidence basis and reference to count as met, partial or unmet.

### Save, resume and compare your own work

Return to Evaluate to reopen saved needs profiles, comparisons and evaluations. Evaluations support autosave, Save now and retry; confirm the saved state before leaving. Use Compare for published-profile needs fit and the saved-evaluations comparison for your own PoC work. Historical evaluations retain their creation version and legacy scoring by default rather than being silently rewritten.

## 10. Principles and boundaries

Needs first. Judge the named offering against the buyer's work, operating model and constraints, not the size of the vendor's portfolio or its marketing category.

Claims are not findings. General availability is release status, not proof of effectiveness. Keep vendor declarations, documentation, demonstrations and environment validation distinguishable.

A profile, not a leaderboard. Report meaningful differences by capability and lifecycle area. Do not use a blended maturity label to hide a weak must-have or compensate for a governance gap.

Human work remains visible. Manual capability is not absent capability. In MDR, work delivered by the provider's analysts must not be relabelled as autonomous product functionality.

Unknown stays unknown. Missing information does not establish success or failure. Record what still needs checking and why.

Scope honestly. Keep unsupported must-haves in the evaluation as gaps. Exclude only genuinely out-of-scope criteria, and compare vendors on the same basis.

Version the evidence. Record the framework, scoring engine, offering, profile revision and relevant references. Revisit findings when the criterion, offering or published profile changes.

Plain language. Explain what is evaluated, how delivery works and what the evidence supports. Avoid marketing superlatives and unqualified claims of autonomy.

## 11. Limitations and publication status

ASEF structures evaluation; it does not certify a vendor or guarantee a result. The following boundaries matter when reading a profile or planning a PoC.

A short research briefing cannot validate production reliability, full detection accuracy or every integration. Treat a demo as observed evidence within its conditions, not as equivalent to deployment in your environment.

Needs-based tailoring is available through environment, scope, priorities, success criteria and autonomy targets. It is not a complete automatic assessment of your telemetry or architecture. Verify integration depth, permissions and operational dependencies during evaluation.

Research publication notice (October 6, 2026): around 40 vendors are undergoing in-depth evaluation. Full technical profiles are planned for November 2026, subject to completed reviews and vendor publication approvals. This is a dated publication plan, not a claim that every profile is available. Check the platform for current availability.

Legacy compatibility has limits. Pre-ASEF 3 evaluations retain their original scoring by default. A saved rating without delivery status may still contribute to a legacy-compatible rating view, but it does not establish recorded GA coverage. Confirm availability and evidence before using it in a current purchasing decision.

A PoC can test the buyer's success criteria on representative scenarios. It does not establish universal detection accuracy across every environment. Record the test conditions, sample limitations and any dependencies that could change the result.

## 12. Acknowledgements and contributing

ASEF builds on ARMM's action catalogue and human-involvement concepts while using a different current evaluation approach. It no longer treats Builder implementation-risk scores as a proxy for product quality.

Thanks to Andrei Cotaie and Cristian Miron for their contributions to ARMM, and to Anton Chuvakin and Rafal Kitab for their contributions to ASEF.

Anton Chuvakin and Oliver Rochford's discussion of AI SOC failure modes in When Marketing Fails informed the framework's attention to inconclusive outcomes, overrides and transparent product limitations.

The framework is practitioner-led and evolves through capability corrections, clearer questions and evidence from real evaluations. Contributors improve the method; inclusion or contribution does not confer a favorable vendor assessment.

### Contributing

Propose capability definitions, clearer examples or methodology corrections through [GitHub contribution forms](https://github.com/secops-unpacked/asef/issues/new/choose) or the [SecOps Unpacked contribution page](https://secops-unpacked.ai/asef/contribute). Use the platform for vendor-fact corrections. Explain what the proposed change measures and why it matters. Keep persistent capability IDs and existing evaluation history intact when terminology changes.

### How to cite

Stojkovski, F. (2026). ASEF: AI SecOps Evaluation Framework, v3.1.3. SecOps Unpacked. Public documentation revision 2026-10-06.1. https://github.com/secops-unpacked/asef
