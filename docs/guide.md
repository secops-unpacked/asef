# Practical guide

ASEF helps answer: **Which offering fits the work my team needs done, and what evidence supports that conclusion?**

You do not need to follow one mandatory funnel. Pick the route that matches your task.

## 1. Start with your needs

Describe your operating model: an internal SOC, an outsourced service, or a team building its capabilities. List the SIEM, MDR, SOAR and other tools you intend to keep, augment or replace.

Choose the work you need across the Shift Map. Mark capabilities Must-have, Nice-to-have, Explore or Out of scope. Write a concrete success criterion for each important requirement.

For example: “Enrich an identity alert using our identity provider and asset inventory, show the source and freshness of each fact, and let us exclude sensitive fields.”

Record deployment, integrations, governance, customer engineering capacity and the desired autonomy for each capability. Keep approval requirements explicit. Do not remove a must-have simply because a vendor cannot meet it.

## 2. Choose technology, MDR, or both

**Technology:** evaluate a named product the customer can operate. Ask what ships, what must be configured, what must be built, and who maintains it.

**MDR:** evaluate a named service package. Ask what the provider actually does, which tools and data sources it supports, how humans and automation share the work, and where its responsibility ends.

**Both:** keep two offering profiles. Internal tools used by an MDR provider are not automatically products a customer can buy or operate. [MDR guide](mdr.md).

## 3. Discover or bring your own shortlist

On the platform, Needs can suggest vendors using available directory and offering facts. A suggestion is a lead for evaluation, not an endorsement or verified capability score.

If you already know the vendors, go directly to their profiles or your own evaluation. A missing published technical profile means information is unavailable; it does not prove a capability is absent.

## 4. Read an offering without scoring it

Published profiles can help you understand product scope, delivery, autonomy and limitations. Vendor approval confirms the publication version and consent; it does not independently validate every claim.

A short briefing, a published profile and a customer PoC have different evidence strength. Do not treat them as interchangeable.

## 5. Compare against the same needs

Compare technology with technology and MDR with MDR, using the same requirements and scope. Review current evidence and record Met, Partially met, Unmet or Unknown for each criterion.

Keep delivery dependencies visible. A customer-build path and a pre-built capability can both be generally available, but they impose different work on your team.

The needs-fit summary counts must-haves with reviewed evidence. A vendor claim alone remains Unknown. Record evidence references and the offering revision. [Worked comparison](../examples/README.md).

## 6. Run your own PoC when needed

Select representative cases and the capabilities you need to verify. Record the configuration, data sources, conditions, approvals, failures and evidence. Use the same scope across vendors.

Record autonomy separately from whether the required outcome was achieved. Level 0 means manual work, not missing information. Automation can be deterministic, AI-driven, or a combination.

Evaluate Platform and Trust as part of the selected offering. A good investigation demo does not establish tenant isolation, safe tool permissions or data-retention compliance.

## 7. Decide and preserve the record

Read fit, coverage, autonomy, customer effort, trust and unresolved gaps together. There is no universal “best vendor” number.

In the platform, return to Evaluate to find saved work. Confirm the saved state before leaving; Save now is available alongside autosave. Historical evaluations retain their version and should not silently inherit new scoring.

ASEF ends at evidence-backed evaluation. Measuring realized financial value after implementation is a separate activity.
