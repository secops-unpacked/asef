# Scoring and interpretation

ASEF keeps delivery, coverage, autonomy, evidence and requirement fit separate. These calculations describe different things. They are not inputs to one universal vendor score.

## Technology capability measures

Lifecycle autonomy codes are `0`, `1C`, `1G`, `1A`, `2`, worth 0, 1, 1, 1, 2 points. Platform and Trust uses functional `0`, `1`, `2`, worth 0, 1, 2 points.

- **Rated depth:** points / (2 × rated capabilities) × 100. With no ratings, the result is absent, not a failing zero.
- **Current GA coverage:** in-scope capabilities with recorded generally available delivery / all in-scope capabilities × 100. Manual GA work counts as present. A Platform and Trust check also needs positive functional support.
- **Full automation:** lifecycle capabilities rated `2` after delivery normalization / all in-scope lifecycle capabilities × 100. Platform functionality is not autonomous execution.
- **Distribution and delivery counts:** keep the ratings and delivery paths visible alongside percentages.

GA includes out-of-the-box, configured, customer-built and required-partner delivery. GA coverage is therefore **not out-of-the-box coverage** and is not verified effectiveness.

Preview and roadmap ratings do not contribute to current ratings or coverage. Unsupported is normalized to zero. Unanswered checks remain unrated. For compatibility with current application behavior, an explicit saved rating with unrecorded delivery can contribute to rated depth, but never establishes recorded GA coverage. The reference tool flags those records.

The platform warning appears when assessed Platform and Trust depth is below 50%. It is a warning, not a certification threshold. Always review the assessed count and individual controls.

The reference groups by `sourceZone` to preserve current application behavior. Display guidance in `shiftMapStages` must not silently migrate saved scoring. See [catalogue boundaries](catalogue.md).

## Needs-fit findings

The comparison counts **Must-have** criteria as Met, Partially met, Unmet or Unknown. Nice-to-have and Explore criteria remain context but do not enter that tally. Out-of-scope checks do not belong in the denominator.

A recorded outcome must match the exact success criterion and current needs/profile/track/revision. It needs a reviewed evidence basis and a non-empty evidence reference. A vendor claim alone remains Unknown. If the profile revision or success criterion changes, reassess rather than carrying old findings forward as current proof.

These are structural safeguards, not automatic truth verification. A person must assess the evidence. A string in `evidenceReference` is not proof by itself.

Technology and MDR are compared separately. Provider-human delivery must not become software autonomy points. The reference supports MDR needs-fit counts, not an invented blended MDR autonomy score.

## Reference tool boundary

`scripts/reference.py` is a small offline illustration. It accepts only the documented public example format and framework baseline 3.1.3. It does not implement the full app, historical ASEF 2 scoring, recommendation algorithms, priority wildcards, questionnaire conditional rendering, consent enforcement or database imports.

In this format, all `capabilityIds` are explicitly selected in scope; missing assessments remain unanswered. Rating codes are strings, including `"0"` and `"2"`. Application backups use a different contract and must not be fed directly to this tool.

See the [fictional examples](../examples/README.md). There are no ROI formulas, Builder T/C/I product scores or Explorer-to-Expert product rankings in this reference.
