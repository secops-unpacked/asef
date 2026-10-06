# Detailed technology checks

Generated from [technology-capabilities.json](../data/technology-capabilities.json). Edit the JSON definitions, then regenerate this document. Do not score everything by default: select checks relevant to your needs.

IDs and source groupings preserve compatibility. Display guidance can differ from historical grouping; see [catalogue boundaries](catalogue.md).

## Data foundation (source grouping)

| ID | Capability and evaluation question | Current display guidance |
| --- | --- | --- |
| `far_left.onboarding.source-onboarding` | **Source onboarding**. Connect a new log source without professional services. | Data foundation |
| `far_left.parsing.parser-generation` | **Parser generation**. Generate a parser for a new or custom log format. | Data foundation |
| `far_left.parsing.normalization-common-model` | **Normalization to a common model**. Map parsed fields into a shared schema such as OCSF or ECS. | Data foundation |
| `far_left.schema.field-schema-mapping` | **Field and schema mapping**. Map source fields to the common schema and flag unmapped fields. | Data foundation |
| `far_left.quality.log-quality-completeness` | **Log quality and completeness assessment**. Assess whether a source is complete, timely, and well formed. | Data foundation |
| `far_left.quality.data-gap-identification` | **Data gap identification**. Identify missing or under-covered sources against expected telemetry. | Data foundation |
| `far_left.routing.ingest-time-enrichment` | **Ingest-time enrichment**. Enrich events at ingestion with identity, asset, or geo context. | Data foundation |
| `far_left.routing.routing-filtering` | **Routing and filtering**. Route, drop, or tier events by value before indexing. | Data foundation |

## Detection and readiness (source grouping)

| ID | Capability and evaluation question | Current display guidance |
| --- | --- | --- |
| `left.author.author-from-description` | **Detection authoring from description**. Generate detection logic from a plain description. | Detection and readiness |
| `left.author.rule-logic-understanding` | **Rule logic understanding**. Read and explain existing detection logic. | Detection and readiness |
| `left.author.query-translation` | **Query translation across SIEM languages**. Translate detection logic between SIEM query languages. | Detection and readiness |
| `left.coverage.mitre-mapping` | **MITRE ATT&CK coverage mapping**. Map current detections to ATT&CK and surface gaps. | Detection and readiness |
| `left.coverage.gap-recommendation` | **Coverage gap recommendation**. Recommend detections to close mapped coverage gaps. | Detection and readiness |
| `left.tuning.fp-tuning` | **False positive tuning**. Tune rules to cut false positives. | Detection and readiness |
| `left.tuning.noisy-rule-identification` | **Noisy-rule identification**. Surface rules generating disproportionate noise. | Detection and readiness |
| `left.dac.detection-as-code` | **Detection as code and version control**. Manage detections as versioned, reviewable code. | Detection and readiness |
| `left.validation.testing-bas` | **Detection testing and validation**. Validate detections with breach and attack simulation. | Detection and readiness |
| `left.validation.decay-drift` | **Detection decay and drift management**. Detect and manage detection decay and drift over time. | Detection and readiness |

## Investigation and understanding (source grouping)

| ID | Capability and evaluation question | Current display guidance |
| --- | --- | --- |
| `mid.context.internal-ingest` | **Internal context ingestion**. Pull past incidents, wikis, and chat into the investigation. | Investigation and understanding |
| `mid.context.case-mgmt-connection` | **Case management connection**. Read and write the case system of record. | Investigation and understanding |
| `mid.enrich.external-ti` | **External threat intel enrichment**. Enrich entities with external threat intelligence. | Investigation and understanding |
| `mid.correlate.dedup-cluster` | **Alert dedup and clustering**. Group related alerts into a single incident. | Investigation and understanding |
| `mid.correlate.timeline` | **Timeline reconstruction**. Build an ordered timeline of events. | Investigation and understanding |
| `mid.correlate.blast-radius` | **Blast radius scoping**. Determine the full scope of affected assets and identities. | Investigation and understanding |
| `mid.engine.guided-investigation` | **Guided investigation steps**. Run investigation steps toward a conclusion. | Investigation and understanding |
| `mid.verdict.tp-fp-btp` | **Verdict (TP/FP/BTP)**. Assign true positive, false positive, or benign true positive. | Investigation and understanding |
| `mid.verdict.confidence` | **Confidence scoring**. Attach a confidence level to the verdict. | Investigation and understanding |
| `mid.verdict.auto-close-reversal` | **Auto-close with reversal tracking**. Auto-close cases and track later reversals. | Investigation and understanding |
| `mid.verdict.escalation-routing` | **Escalation routing**. Route cases to the right responder or queue. | Investigation and understanding |

## Remediation and improvements (source grouping)

| ID | Capability and evaluation question | Current display guidance |
| --- | --- | --- |
| `right.identity.group-adherence` | **Group Adherence**. Add or remove an account from a group. | Remediation and improvements |
| `right.identity.label-user` | **Label User (Tagging)**. Tag or label a user account. | Remediation and improvements |
| `right.identity.revoke-sessions` | **Revoke Sessions**. Revoke active user sessions. | Remediation and improvements |
| `right.identity.reset-password-standard` | **Reset Password (Standard)**. Reset a standard user's password. | Remediation and improvements |
| `right.identity.disable-standard-user` | **Disable Standard User**. Disable a standard user account. | Remediation and improvements |
| `right.identity.delete-sharing-permissions` | **Delete Sharing Permissions**. Remove sharing permissions from resources. | Remediation and improvements |
| `right.identity.remove-specific-permissions` | **Remove Specific Permissions**. Remove a specific set of permissions. | Remediation and improvements |
| `right.identity.group-creation` | **Group Creation**. Create a new security group. | Remediation and improvements |
| `right.identity.disable-service-principals` | **Disable Service Principals**. Disable a service account, service principal, or managed identity. | Remediation and improvements |
| `right.identity.reset-vip-password` | **Reset VIP Password**. Reset password for C-suite or VP level users. | Remediation and improvements |
| `right.identity.rotate-secrets-production` | **Rotate Secrets (Production)**. Create or rotate secrets and tokens in production. | Remediation and improvements |
| `right.network.block-port` | **Block Port**. Block a specific port. | Remediation and improvements |
| `right.network.connection-reset` | **Connection Reset**. Reset a network connection. | Remediation and improvements |
| `right.network.sinkhole-traffic` | **Sinkhole Traffic**. Sinkhole traffic to a specific destination. | Remediation and improvements |
| `right.network.disconnect-host` | **Disconnect Host**. Disconnect a host from the network. | Remediation and improvements |
| `right.network.quarantine-device` | **Quarantine Device**. Quarantine a device at network level. | Remediation and improvements |
| `right.network.firewall-rule-creation` | **Firewall Rule Creation**. Create a new firewall rule. | Remediation and improvements |
| `right.network.modify-nat-rules` | **Modify NAT Rules**. Change NAT rules to modify traffic patterns. | Remediation and improvements |
| `right.network.vlan-creation` | **VLAN Creation**. Create a new VLAN on the network. | Remediation and improvements |
| `right.network.move-host-isolated-vlan` | **Move Host to Isolated VLAN**. Move a device to a restricted VLAN. | Remediation and improvements |
| `right.network.routing-table-change` | **Routing Table Change**. Change a routing table entry. | Remediation and improvements |
| `right.network.quarantine-enterprise-server` | **Quarantine Enterprise Server**. Quarantine a server running an enterprise service. | Remediation and improvements |
| `right.endpoint.malware-scan-forensics` | **Malware Scan / Forensics**. Initiate a scan or forensics collection on device. | Investigation and understanding |
| `right.endpoint.clear-browser-cache` | **Clear Browser Cache**. Remove files, cookies, data from browser cache. | Remediation and improvements |
| `right.endpoint.collect-memory-dump` | **Collect Memory Dump**. Initiate and retrieve a memory dump forensically. | Investigation and understanding |
| `right.endpoint.kill-process` | **Kill Process**. Terminate a running process. | Remediation and improvements |
| `right.endpoint.block-file-hash` | **Block File (via Hash)**. Block a file by its hash. | Remediation and improvements |
| `right.endpoint.lock-out-local-user` | **Lock Out Local User**. Lock out a user from the local device. | Remediation and improvements |
| `right.endpoint.block-removable-drive` | **Block Removable Drive**. Block removable storage devices. | Remediation and improvements |
| `right.endpoint.isolate-device` | **Isolate Device**. Isolate a device from reaching out. | Remediation and improvements |
| `right.endpoint.remove-device-from-domain` | **Remove Device from Domain**. Remove a device from the domain. | Remediation and improvements |
| `right.endpoint.deploy-remediation-script` | **Deploy Remediation Script**. Deploy a script or application for remediation. | Remediation and improvements |
| `right.cloud.copy-storage-device` | **Copy Storage Device**. Create a copy of cloud storage for forensic investigation. | Investigation and understanding |
| `right.cloud.mount-storage-device` | **Mount Storage Device**. Mount new storage to a VM for forensics. | Investigation and understanding |
| `right.cloud.snapshot-vm-db` | **Snapshot VM / DB**. Create a snapshot of current state. | Remediation and improvements |
| `right.cloud.enable-diagnostic-settings` | **Enable Diagnostic Settings**. Alter settings for advanced log gathering. | Remediation and improvements |
| `right.cloud.remove-permissions-resource` | **Remove Permissions to Resource**. Remove a service principal or managed identity from a resource. | Remediation and improvements |
| `right.cloud.modify-security-group-rules` | **Modify Security Group Rules**. Modify firewall rules on a cloud resource. | Remediation and improvements |
| `right.cloud.modify-access-type` | **Modify Access Type**. Switch resource from public to private. | Remediation and improvements |
| `right.cloud.stop-resource` | **Stop a Resource**. Stop a resource from execution. | Remediation and improvements |
| `right.cloud.apply-resource-lock` | **Apply Resource Lock**. Make the resource immutable or read-only. | Remediation and improvements |
| `right.cloud.create-security-group` | **Create a Security Group**. Create and apply a new security group. | Remediation and improvements |
| `right.cloud.isolate-resource` | **Isolate Resource**. Quarantine a cloud resource. | Remediation and improvements |
| `right.cloud.modify-keyvault-entries` | **Modify KeyVault Entries**. Add or modify resources in a KeyVault. | Remediation and improvements |
| `right.cloud.remove-files-storage-buckets` | **Remove Files from Storage Buckets**. Remove files from cloud storage containers. | Remediation and improvements |
| `right.cloud.delete-resource` | **Delete Resource**. Delete a resource from the cloud environment. | Remediation and improvements |
| `right.cloud.use-breakglass-account` | **Use Breakglass Account**. Use a breakglass account in case of emergency. | Remediation and improvements |
| `right.saas.grab-email-sample` | **Grab Email Sample**. Grab an attached file from an email. | Investigation and understanding |
| `right.saas.grab-email-link` | **Grab Email Link**. Grab a link from inside an email message. | Investigation and understanding |
| `right.saas.quarantine-email` | **Quarantine Email**. Move email to quarantine or junk. | Remediation and improvements |
| `right.saas.delete-email` | **Delete Email**. Remove an email from the user's mailbox. | Remediation and improvements |
| `right.saas.create-email-routing-rule` | **Create Email Routing Rule**. Create rules to handle and route incoming email. | Remediation and improvements |
| `right.saas.disable-malicious-inbox-rule` | **Disable Malicious Inbox Rule**. Disable a malicious rule in a user's mailbox. | Remediation and improvements |
| `right.saas.block-sender` | **Block Sender**. Block a sender from the domain. | Remediation and improvements |
| `right.saas.add-remove-meeting-invite` | **Add / Remove Meeting Invite**. Modify a user's calendar. | Remediation and improvements |
| `right.saas.modify-user-status-hr` | **Read / Modify User Status (HR)**. Read or modify user status in HR platform. | Remediation and improvements |
| `right.saas.modify-hr-records` | **Modify HR Records**. Modify HR records beyond status. | Remediation and improvements |
| `right.feedback.post-incident-summary` | **Post-incident summary and lessons**. Generate a post-incident summary with lessons learned. | Feedback and implemented improvements |
| `right.feedback.analyst-feedback-mechanism` | **Feedback mechanism**. Let analysts confirm, reject, or correct automated outcomes. | Feedback and implemented improvements |
| `right.feedback.improvement-suggestions` | **Improvement suggestions from closed cases**. Suggest detection and process improvements from closed cases. | Feedback and implemented improvements |

## Platform and Trust (source grouping)

| ID | Capability and evaluation question | Current display guidance |
| --- | --- | --- |
| `platform.ops.close-alerts-siem` | **SIEM alert bidirectional updates**. Can the product receive alert changes from the SIEM and write updates back? Specify which fields sync in each direction, such as status, verdict, severity, notes, and reopened alerts. Closing an alert alone is only partial support. | Platform and Trust |
| `platform.ops.alerting` | **Responder notifications and escalation**. How does the product notify the right responder when a case needs attention or approval? Identify the supported channels, routing rules, and escalation options. | Platform and Trust |
| `platform.ops.native-chat-integration` | **Slack and Teams case collaboration**. Can analysts review cases, add context, and approve or reject actions in Slack or Teams? Distinguish two-way case interaction from one-way notifications. | Platform and Trust |
| `platform.ops.stats-health-dashboards` | **Platform and integration health dashboards**. Can customers see connector health, processing delays, failed workflows, and platform usage? Explain which dashboards ship with the product and which customers must build. | Platform and Trust |
| `platform.ops.investigation-audit-trail` | **Case activity and approval audit trail**. Can a customer reconstruct a case from its inputs, queries, decisions, approvals, and actions? Explain what is recorded, how long it is retained, and whether it can be exported. | Platform and Trust |
| `platform.ops.ir-metrics-tracking` | **Incident response performance metrics**. Which response metrics can customers track over time, such as time to triage, investigate, and contain? Explain the definitions, reporting filters, and export options. | Platform and Trust |
| `platform.ops.logging` | **Platform activity and error logs**. Can customers access and export logs of user activity, API calls, connector failures, and workflow errors? Explain the search, retention, and troubleshooting options. | Platform and Trust |
| `platform.ops.ease-of-use-gui` | **Analyst interface and everyday workflows**. Can analysts review evidence, investigate cases, and manage response actions through the interface? Identify routine tasks that still require code, APIs, or vendor assistance. | Platform and Trust |
| `platform.ops.account-management-sso` | **Single sign-on and user account management**. Which identity providers and single sign-on methods are supported? Explain how customers provision users, remove access, and enforce their authentication policies. | Platform and Trust |
| `platform.ops.support-level` | **Vendor support coverage and response times**. What support is included, during which hours, and with what response commitments? Identify the escalation process and any support that requires a higher subscription. | Platform and Trust |
| `platform.ops.feedback-loop-mechanism` | **Analyst feedback collection and improvement**. How are analyst corrections and case feedback collected and used to improve the product? Distinguish manual feedback, automatic learning, and changes that require customer approval. | Platform and Trust |
| `platform.ops.auto-close-reversal-tracking` | **Auto-closed case review and reversal reporting**. Can customers review cases closed automatically and track those later reopened or overturned? Explain whether review reports are scheduled, how reversals are recorded, and how missed incidents are surfaced. | Platform and Trust |
| `platform.ops.roles-and-responsibilities` | **Role-based access and action permissions**. Can customers control who can view cases, change configuration, approve actions, and execute responses? Describe the permission granularity and separation of responsibilities. | Platform and Trust |
| `platform.ops.api-development` | **Documented APIs for customer integrations**. Which product functions and data are available through documented APIs? Explain how customers build integrations, including authentication, permissions, rate limits, and API versioning. | Platform and Trust |
| `platform.trust.reasoning-logging` | **Recorded decision rationale**. Does the product retain a reviewable explanation for each automated decision? Identify the inputs, rules or models used, and stated reasons recorded alongside the decision. | Platform and Trust |
| `platform.trust.explainability-decision-transparency` | **Evidence-backed verdict and action explanations**. Can an analyst see why the product reached a verdict or chose an action? Explain how conclusions link to source evidence and how uncertainty or conflicting evidence is shown. | Platform and Trust |
| `platform.trust.ai-decision-accuracy-reporting` | **Decision accuracy and error reporting**. Can customers measure correct and incorrect verdicts, missed incidents, and inconclusive results? Explain how outcomes are verified and whether the underlying data can be exported for independent review. | Platform and Trust |
| `platform.trust.bring-your-own-model` | **Customer-provided AI models**. Can customers connect a model or model endpoint they control? Identify supported providers or hosting options, which functions can use them, and any limitations. | Platform and Trust |
| `platform.trust.context-grounding` | **Decisions grounded in customer context**. Which customer context informs decisions, such as past cases, asset criticality, identities, and business processes? Explain how it is gathered, kept current, and linked to the resulting conclusions. | Platform and Trust |
| `platform.trust.autonomous-action-thresholds` | **Granular autonomy limits and approval controls**. Can customers set what runs unattended and what needs approval by alert type, data source, severity, asset, or action? Cover automation, AI reasoning, and combinations of both, including overrides and emergency stops. | Platform and Trust |
| `platform.trust.model-drift-detection` | **Model quality monitoring and drift alerts**. How does the product detect declining accuracy or changes in model behavior over time? Explain what is monitored, how customers are notified, and how they can respond. | Platform and Trust |
| `platform.trust.adversarial-robustness-testing` | **Prompt injection and tool misuse testing**. How is the product tested against malicious instructions in alerts, retrieved content, or tool output? Describe protections against unsafe tool use and what test results customers can review. | Platform and Trust |
