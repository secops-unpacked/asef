# Governance

## Stewardship

Filip Stojkovski / SecOps Unpacked is the maintainer and approves changes to the official framework baseline. Contributors advise, propose and review. Attribution does not imply that a contributor endorses every subsequent change or vendor evaluation.

## Decision criteria

A change should improve practitioner understanding, testability, evidence quality or fair comparison. It should distinguish technology from service, describe delivery dependencies, retain uncertainty, and avoid rewarding more autonomy without regard to the buyer's needs.

For substantive changes, record:

1. The problem and proposed definition.
2. Practical examples and counterexamples.
3. Evidence and relevant affiliations.
4. Effects on IDs, scoring, old evaluations and public profiles.
5. The maintainer's decision and rationale.

New capability IDs and changed calculation semantics require explicit review and versioning. Editorial corrections do not automatically constitute a new scoring release.

## Independence and public/private boundaries

Vendors can contribute. Sponsorship, subscriptions and advisory relationships do not purchase favorable scores or placement. Reviewers should disclose relevant affiliations and avoid presenting a vendor's preferred wording as established fact.

The repository describes the method, not private research verdicts. Publication of a vendor profile remains a separate process requiring the appropriate consent, exact-version review and approval. A contributor cannot publish someone else's RFI by attaching it to an issue.

## Releases and synchronization

Approved public releases are versioned references. Google Docs can remain a drafting/review surface; the hosted platform remains an implementation with its own deployment process. [Maintenance policy](docs/maintenance.md) explains how to keep them aligned.

Do not overwrite a historical release to change the meaning of a completed evaluation. Retain deprecated IDs and document replacements instead of recycling them.

## Review controls

The repository includes a CODEOWNERS file and automated validation. CODEOWNERS requests review; it does not itself enforce branch protection. Changes after the initial publication should arrive through pull requests. Maintainers should enable required review and validation checks in repository rules before accepting external code contributions.
