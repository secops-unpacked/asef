# MDR service questionnaire

Generated from [mdr-questions.json](../data/mdr-questions.json). Edit the JSON definitions, then regenerate this document.

Evaluate a named service package. Human delivery is not software autonomy. A section marked Roadmap only or Not offered requires only its availability declaration; optional notes remain available. See the [MDR guide](mdr.md) for interpretation.

## Sources and customer environment

Where cases and evidence come from, including the customer's existing SIEM and employee requests.

### Is this included in the evaluated service?

ID: `mdr.sources.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### Where can the service receive cases and evidence?

ID: `mdr.sources.intake`. Required when this section is offered.

Separate incoming alerts from direct telemetry and customer requests.

**Example:** We ingest SIEM incidents, query EDR evidence directly and accept employee-reported phishing.

Select all that apply.

- Customer SIEM / data lake (`siem`)
- Directly from EDR, NDR, identity or other detection tools (`detection_tools`)
- Raw telemetry (`raw_telemetry`)
- Ticketing / API / webhook (`tickets`)
- Employee reports or custom investigation requests (`employee`)
- Provider's own detection stack (`own_stack`)

### Can you operate over the customer's existing SIEM?

ID: `mdr.sources.siem`. Required when this section is offered.

State whether the SIEM stays in place and who operates it.

**Example:** The customer keeps its SIEM; we consume alerts, query evidence and write back case updates.

Select one.

- Yes, as an overlay (`overlay`)
- Yes, we operate or co-manage their SIEM (`operate`)
- Overlay or co-managed operation (`both`)
- No, requires our own stack (`own_only`)
- SIEM is not required or used (`no_siem`)

### Who connects and maintains sources?

ID: `mdr.sources.integrations`. Required when this section is offered.

Include connector maintenance and missing-telemetry handling, not just initial setup.

**Example:** Our team maintains shipped connectors; custom sources require customer engineering.

Select one.

- Provider handles onboarding and maintenance (`provider`)
- Shared with the customer (`shared`)
- Customer builds or maintains connections (`customer`)
- Partner handles connections (`partner`)

### Can employees or the SOC submit custom investigation requests?

ID: `mdr.sources.requests`. Required when this section is offered.

Include suspicious activity that did not generate an alert.

**Example:** An employee reports an unusual MFA prompt through Teams and our analysts investigate.

Select one.

- Employee and SOC requests (`both`)
- SOC requests only (`soc`)
- Employee reports only (`employee`)
- Not supported (`no`)

### Who or what performs this work?

ID: `mdr.sources.execution`. Required when this section is offered.

Distinguish provider humans, deterministic automation, ML and LLM or agent reasoning.

**Example:** An LLM proposes queries, integrations execute them, and an analyst approves containment.

Select all that apply.

- Provider human analysts (`human`)
- Deterministic automation (`automation`)
- Machine learning (`ml`)
- LLM / agent reasoning (`llm`)

### How are the provider's humans involved?

ID: `mdr.sources.oversight`. Required when this section is offered.

Provider oversight is separate from customer delegation or approval.

**Example:** The customer pre-authorizes containment, but a provider analyst approves each execution.

Select one.

- Human approval required before execution (`in_loop`)
- Runs within policy; human supervises and can intervene (`on_loop`)
- Runs without case-by-case human involvement (`unattended`)
- Human performs the work (`manual`)
- Varies by activity; explain below (`mixed`)

### Customer work, limits and evidence

ID: `mdr.sources.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.

## Detection engineering and hunting

What you build, maintain and proactively hunt for, and what the customer can see or change.

### Is this included in the evaluated service?

ID: `mdr.detection.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### Where do you develop and maintain detections?

ID: `mdr.detection.development`. Required when this section is offered.

Distinguish provider-owned detections from detections deployed into customer tooling.

**Example:** We tune rules in the customer's SIEM and maintain our own cross-customer detection content.

Select one.

- Our stack and customer tools (`both`)
- Our stack only (`provider`)
- Customer tools only (`customer`)
- We do not develop detections (`none`)

### Can customers inspect and change detection logic?

ID: `mdr.detection.customer_access`. Required when this section is offered.

Describe actual permissions, not just visibility of detection names.

**Example:** Customers can read the rule, request changes, and export it; they cannot edit production rules directly.

Select one.

- View, edit and export (`edit_export`)
- View and edit, no export (`edit`)
- View and export, changes by request (`view_export`)
- View, changes by request (`view_request`)
- Changes by request; logic not visible (`request`)
- Neither visible nor editable (`none`)
- No detection development (`na`)

### Which threat hunts do you deliver?

ID: `mdr.detection.hunts`. Required when this section is offered.

Reactive hunts follow an incident; proactive hunts do not require an existing alert.

**Example:** We hunt after escalations and run campaigns based on new threat intelligence.

Select all that apply.

- Reactive / incident-driven (`reactive`)
- Proactive / hypothesis-led (`proactive`)
- Threat-intelligence-report driven (`intel`)
- Scheduled hunts (`scheduled`)
- Customer-requested or manually launched (`requested`)
- No threat hunting (`none`)

### How are hunt findings tracked?

ID: `mdr.detection.tracking`. Required when this section is offered.

Explain whether campaigns have owners and actions through to completion.

**Example:** Each campaign links findings to detection changes with an owner and completion status.

Select one.

- Campaigns, findings, owners and follow-up actions (`tracked`)
- Hunt reports without tracked follow-up (`reports`)
- Individual cases only (`cases`)
- No hunting / tracking (`none`)

### Who or what performs this work?

ID: `mdr.detection.execution`. Required when this section is offered.

Distinguish provider humans, deterministic automation, ML and LLM or agent reasoning.

**Example:** An LLM proposes queries, integrations execute them, and an analyst approves containment.

Select all that apply.

- Provider human analysts (`human`)
- Deterministic automation (`automation`)
- Machine learning (`ml`)
- LLM / agent reasoning (`llm`)

### How are the provider's humans involved?

ID: `mdr.detection.oversight`. Required when this section is offered.

Provider oversight is separate from customer delegation or approval.

**Example:** The customer pre-authorizes containment, but a provider analyst approves each execution.

Select one.

- Human approval required before execution (`in_loop`)
- Runs within policy; human supervises and can intervene (`on_loop`)
- Runs without case-by-case human involvement (`unattended`)
- Human performs the work (`manual`)
- Varies by activity; explain below (`mixed`)

### Customer work, limits and evidence

ID: `mdr.detection.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.

## Enrichment and organizational context

How context is gathered, maintained and used. A graph is an architecture choice, not a score.

### Is this included in the evaluated service?

ID: `mdr.context.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### What context do you gather?

ID: `mdr.context.sources`. Required when this section is offered.

Include security history and business context; avoid claiming sources only available through custom work.

**Example:** We use previous incidents, identity privileges, asset owners and business criticality.

Select all that apply.

- Security telemetry and alerts (`security`)
- Past cases and decisions (`cases`)
- Identity, privileges and relationships (`identity`)
- Assets and vulnerabilities (`assets`)
- Business owners, processes and criticality (`business`)
- Employee clarifications (`employees`)
- Threat intelligence (`intel`)
- No enrichment (`none`)

### How is context stored or retrieved?

ID: `mdr.context.architecture`. Required when this section is offered.

A graph, database or live lookup can all be valid. Describe the implementation rather than its marketing name.

**Example:** Relationships are stored in a graph; historical case text is retrieved from a vector index.

Select one.

- Knowledge / context graph (`graph`)
- Database / case records (`database`)
- Vector retrieval (`retrieval`)
- Live queries without a persistent context store (`live`)
- Combination (`hybrid`)
- No persistent or retrieved context (`none`)

### How is customer context kept accurate?

ID: `mdr.context.maintenance`. Required when this section is offered.

Who refreshes it and can the customer correct it? Explain stale or conflicting evidence in the optional details.

**Example:** Connectors refresh asset records daily and customers can correct asset criticality.

Select one.

- Automatic refresh and customer corrections (`sync_edit`)
- Automatic refresh; corrections via our team (`sync_request`)
- Manual maintenance by our team (`manual`)
- Customer maintains it (`customer`)
- No maintained context (`none`)

### Can you use customer history from before onboarding?

ID: `mdr.context.history`. Required when this section is offered.

Distinguish importing historical cases from searching older telemetry.

**Example:** We import previous case decisions and search retained SIEM logs when new indicators emerge.

Select one.

- Import history and run retrospective checks (`both`)
- Import only (`import`)
- Retrospective checks only (`search`)
- Neither (`neither`)

### Who or what performs this work?

ID: `mdr.context.execution`. Required when this section is offered.

Distinguish provider humans, deterministic automation, ML and LLM or agent reasoning.

**Example:** An LLM proposes queries, integrations execute them, and an analyst approves containment.

Select all that apply.

- Provider human analysts (`human`)
- Deterministic automation (`automation`)
- Machine learning (`ml`)
- LLM / agent reasoning (`llm`)

### How are the provider's humans involved?

ID: `mdr.context.oversight`. Required when this section is offered.

Provider oversight is separate from customer delegation or approval.

**Example:** The customer pre-authorizes containment, but a provider analyst approves each execution.

Select one.

- Human approval required before execution (`in_loop`)
- Runs within policy; human supervises and can intervene (`on_loop`)
- Runs without case-by-case human involvement (`unattended`)
- Human performs the work (`manual`)
- Varies by activity; explain below (`mixed`)

### Customer work, limits and evidence

ID: `mdr.context.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.

## Investigation, employees and DFIR

Investigation depth, employee interaction and forensic boundaries.

### Is this included in the evaluated service?

ID: `mdr.investigation.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### What investigation work is delivered?

ID: `mdr.investigation.depth`. Required when this section is offered.

Choose the work the service actually performs, not every capability of an underlying tool.

**Example:** Our team builds a timeline, hunts for related activity and determines affected identities.

Select all that apply.

- Enrichment, correlation and verdict (`triage`)
- Timeline and root-cause analysis (`timeline`)
- Reactive threat hunting (`hunting`)
- Blast radius and affected entities (`scope`)
- Incident coordination (`coordination`)
- No investigation (`none`)

### Can you interact directly with employees?

ID: `mdr.investigation.employees`. Required when this section is offered.

Explain channels, identity verification and privacy controls in the details below.

**Example:** Our analyst contacts the employee through an approved Teams channel to confirm activity, with the conversation linked to the case.

Select one.

- Provider analysts contact employees (`human`)
- AI-assisted messages reviewed by a human (`ai_reviewed`)
- AI interacts directly within approved boundaries (`ai_direct`)
- Only through the customer's SOC (`customer`)
- No employee interaction (`none`)

### What DFIR support is available?

ID: `mdr.investigation.dfir`. Required when this section is offered.

Collection alone is not a full forensic investigation. Include evidence integrity and chain-of-custody limits in the details.

**Example:** Artifact collection is included; full forensic analysis requires a separate retainer.

Select one.

- Full DFIR included (`full`)
- Collection / initial analysis only (`collection`)
- Separate paid DFIR engagement (`add_on`)
- Partner referral (`partner`)
- Not offered (`none`)

### Who or what performs this work?

ID: `mdr.investigation.execution`. Required when this section is offered.

Distinguish provider humans, deterministic automation, ML and LLM or agent reasoning.

**Example:** An LLM proposes queries, integrations execute them, and an analyst approves containment.

Select all that apply.

- Provider human analysts (`human`)
- Deterministic automation (`automation`)
- Machine learning (`ml`)
- LLM / agent reasoning (`llm`)

### How are the provider's humans involved?

ID: `mdr.investigation.oversight`. Required when this section is offered.

Provider oversight is separate from customer delegation or approval.

**Example:** The customer pre-authorizes containment, but a provider analyst approves each execution.

Select one.

- Human approval required before execution (`in_loop`)
- Runs within policy; human supervises and can intervene (`on_loop`)
- Runs without case-by-case human involvement (`unattended`)
- Human performs the work (`manual`)
- Varies by activity; explain below (`mixed`)

### Customer work, limits and evidence

ID: `mdr.investigation.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.

## Response, remediation and handover

Actions delivered, customer-specific processes, approval and where your responsibility ends.

### Is this included in the evaluated service?

ID: `mdr.response.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### Where can the service execute response actions?

ID: `mdr.response.actions`. Required when this section is offered.

Receiving alerts from a tool does not establish the ability to take action in it.

**Example:** We can isolate endpoints and revoke identity sessions, but only recommend network changes.

Select all that apply.

- Endpoint (`endpoint`)
- Identity (`identity`)
- Network (`network`)
- Cloud (`cloud`)
- SaaS / email (`saas`)
- Recommendations only (`none`)

### Where does your responsibility end?

ID: `mdr.response.boundary`. Required when this section is offered.

Choose the normal contracted boundary; describe exceptions below.

**Example:** We contain the threat and verify containment; the customer owns rebuilding affected systems.

Select one.

- Notification / escalation (`notify`)
- Investigation and recommendations (`recommend`)
- Containment and verification (`contain`)
- Remediation and verification (`remediate`)
- Recovery coordination through resolution (`recover`)

### How does the customer authorize response?

ID: `mdr.response.authorization`. Required when this section is offered.

Customer delegation is separate from whether your own analysts approve actions.

**Example:** The customer pre-authorizes endpoint isolation, while account deletion needs specific approval.

Select one.

- Customer approval for each action (`each`)
- Pre-authorized actions within customer policy (`policy`)
- Different approval by action, risk or system (`mixed`)
- No response execution (`none`)

### Can response follow the customer's processes?

ID: `mdr.response.processes`. Required when this section is offered.

Include business-critical exceptions, change windows and approval chains.

**Example:** Production servers require application-owner approval even if workstation isolation is pre-authorized.

Select one.

- Customer-specific processes and playbooks (`custom`)
- Configurable provider templates (`configured`)
- Provider's standard process only (`standard`)
- No response execution (`none`)

### What happens when work is escalated to the customer?

ID: `mdr.response.handover`. Required when this section is offered.

Separate sending a ticket from tracking whether the issue was resolved.

**Example:** We retain the case owner, track customer tasks and verify the result before closure.

Select one.

- We retain ownership through verified resolution (`owned`)
- Shared ownership with tracked follow-up (`shared`)
- Customer takes ownership after handover (`handoff`)
- Depends on the contracted activity; explain below (`varies`)

### Who or what performs this work?

ID: `mdr.response.execution`. Required when this section is offered.

Distinguish provider humans, deterministic automation, ML and LLM or agent reasoning.

**Example:** An LLM proposes queries, integrations execute them, and an analyst approves containment.

Select all that apply.

- Provider human analysts (`human`)
- Deterministic automation (`automation`)
- Machine learning (`ml`)
- LLM / agent reasoning (`llm`)

### How are the provider's humans involved?

ID: `mdr.response.oversight`. Required when this section is offered.

Provider oversight is separate from customer delegation or approval.

**Example:** The customer pre-authorizes containment, but a provider analyst approves each execution.

Select one.

- Human approval required before execution (`in_loop`)
- Runs within policy; human supervises and can intervene (`on_loop`)
- Runs without case-by-case human involvement (`unattended`)
- Human performs the work (`manual`)
- Varies by activity; explain below (`mixed`)

### Customer work, limits and evidence

ID: `mdr.response.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.

## Feedback and implemented improvements

What changes after a case, who approves it and how the customer knows it happened.

### Is this included in the evaluated service?

ID: `mdr.feedback.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### How is feedback collected?

ID: `mdr.feedback.inputs`. Required when this section is offered.

Include mistakes, reopened cases and failed actions, not just satisfaction surveys.

**Example:** Analysts review corrected verdicts and a sample of automatically closed cases weekly.

Select all that apply.

- Customer / analyst corrections (`corrections`)
- Reopened cases (`reopened`)
- Response success, failure or rollback (`actions`)
- Review of AI / automatically closed cases (`sampling`)
- Scheduled customer reviews (`reviews`)
- No structured feedback (`none`)

### What is changed as a result?

ID: `mdr.feedback.changes`. Required when this section is offered.

Select implemented changes, not improvements merely recommended to the customer.

**Example:** A corrected verdict updates a detection exception and a reviewed investigation procedure.

Select all that apply.

- Detections and tuning (`detections`)
- Context / knowledge records (`context`)
- Investigation procedures or prompts (`investigation`)
- Response processes and automation (`response`)
- Models, after validation (`models`)
- Recommendations only (`recommendations`)
- No implemented changes (`none`)

### Can customers see which improvements were implemented?

ID: `mdr.feedback.visibility`. Required when this section is offered.

A report of findings is different from a record of completed changes.

**Example:** The customer sees the change, case reference, approval, validation and deployment date.

Select one.

- Linked change, approval, validation and deployment record (`audited`)
- Summary of changes only (`summary`)
- Available on request (`request`)
- No implementation visibility (`none`)

### Who or what performs this work?

ID: `mdr.feedback.execution`. Required when this section is offered.

Distinguish provider humans, deterministic automation, ML and LLM or agent reasoning.

**Example:** An LLM proposes queries, integrations execute them, and an analyst approves containment.

Select all that apply.

- Provider human analysts (`human`)
- Deterministic automation (`automation`)
- Machine learning (`ml`)
- LLM / agent reasoning (`llm`)

### How are the provider's humans involved?

ID: `mdr.feedback.oversight`. Required when this section is offered.

Provider oversight is separate from customer delegation or approval.

**Example:** The customer pre-authorizes containment, but a provider analyst approves each execution.

Select one.

- Human approval required before execution (`in_loop`)
- Runs within policy; human supervises and can intervene (`on_loop`)
- Runs without case-by-case human involvement (`unattended`)
- Human performs the work (`manual`)
- Varies by activity; explain below (`mixed`)

### Customer work, limits and evidence

ID: `mdr.feedback.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.

## Service transparency and trust

Human versus machine activity, safety, customer visibility and service commitments.

### Is this included in the evaluated service?

ID: `mdr.trust.availability`. Required when this section is offered.

Record the named package boundary. Add-ons and partner delivery are not included service.

**Example:** Reactive hunting is included; proactive hunting requires an add-on.

Select one.

- Included in the evaluated package (`included`)
- Paid add-on; not included (`add_on`)
- Delivered by a named partner (`partner`)
- Roadmap only (`roadmap`)
- Not offered (`not_supported`)

### Can customers distinguish AI, automation and human work?

ID: `mdr.trust.attribution`. Required when this section is offered.

Look for attribution for each decision or action, not an overall AI-powered label.

**Example:** The case timeline identifies the model-generated verdict, automated queries and analyst-approved containment.

Select one.

- Per-step attribution visible to customers (`step`)
- Case-level summary only (`case`)
- Only available on request (`request`)
- Not visible (`none`)

### What happens when AI is uncertain or fails?

ID: `mdr.trust.failure`. Required when this section is offered.

Describe safe fallback, escalation and responsibility, not just model confidence.

**Example:** Conflicting evidence prevents auto-closure and routes the case to an analyst.

Select one.

- Escalates to a human with evidence (`human`)
- Falls back to bounded deterministic procedures (`bounded`)
- Human escalation and bounded fallback (`both`)
- No defined fallback (`none`)
- No AI in the evaluated service (`no_ai`)

### Which safeguards can you demonstrate?

ID: `mdr.trust.controls`. Required when this section is offered.

Select current controls and use the briefing to show evidence. These are declarations, not verified scores.

**Example:** Tool permissions prevent an investigation agent from taking response actions without approval.

Select all that apply.

- Scoped tool permissions and approval controls (`permissions`)
- Testing malicious content in alerts and employee messages (`untrusted`)
- Data residency, retention and tenant isolation (`data`)
- Model and prompt change testing (`models`)
- Evidence-linked audit trail and overrides (`audit`)
- None available to demonstrate (`none`)

### What coverage and service commitments apply?

ID: `mdr.trust.commitments`. Required when this section is offered.

State hours, escalation coverage, targets versus contractual SLAs, and exclusions for this package.

**Example:** 24/7 investigation; containment target measured from confirmed incident. Recovery is not included.

Answer with text.

### Customer work, limits and evidence

ID: `mdr.trust.details`. Optional.

Describe required customer work, dependencies, exceptions and a redacted evidence reference.

**Example:** The customer connects identity sources and approves actions on privileged accounts.

Answer with text.
