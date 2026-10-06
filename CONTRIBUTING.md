# Contributing to ASEF

You do not need to write code. Tell us what should improve, why it matters to a practitioner, and how someone could test it.

## Choose the simplest route

- [Clarify a question or definition](https://github.com/secops-unpacked/asef/issues/new?template=clarification.yml).
- [Propose a capability](https://github.com/secops-unpacked/asef/issues/new?template=capability.yml).
- [Discuss a methodology or scoring change](https://github.com/secops-unpacked/asef/issues/new?template=methodology.yml).
- [Open a discussion](https://github.com/secops-unpacked/asef/discussions) for an idea that is not yet a specific change.
- Prefer not to use GitHub? Use the [platform contribution page](https://secops-unpacked.ai/asef/contribute). The maintainer can summarize a non-confidential proposal here with your permission. There is no automatic form-to-GitHub sync.

## What makes a useful proposal

Give the capability ID or section, describe the problem, propose clearer wording, and include a realistic example or public evidence. Distinguish software from service delivery, shipped capability from custom work, and a vendor claim from a verified result.

Disclose relevant vendor or commercial affiliations. Vendors are welcome; promotional copy and pay-to-rank requests are not contributions to the methodology.

**Everything in public issues and pull requests is public.** Do not submit raw RFIs, customer cases, recordings, credentials, private evaluations or personal contact details. For security or accidental disclosure, use [SECURITY.md](SECURITY.md).

## Propose an edit

For a small wording change, open the file on GitHub and use its edit control to propose a pull request. For a larger methodology change, discuss the proposal first.

For local changes:

```sh
git clone https://github.com/YOUR-ACCOUNT/asef.git
cd asef
git switch -c clarify-capability
# Edit the relevant Markdown or JSON file.
python3 scripts/catalogue_docs.py --write
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Fork the repository to your account before using this example. Never reuse a capability ID for a new meaning. Include examples and tests when definitions or calculations change, and explain effects on existing evaluations.

The detailed technology and MDR question documents are generated from JSON. Edit their definitions first; the command above refreshes the readable versions. Checks will catch drift between the two.

## Review and acceptance

Filip Stojkovski / SecOps Unpacked maintains the official baseline. Public discussion informs decisions; popularity is not evidence and a contribution is not an endorsement. See [governance](GOVERNANCE.md).

Accepted material is published under [CC BY 4.0](LICENSE). By submitting material for inclusion, confirm that you have the necessary rights and agree to that license for your contribution. Do not copy third-party material without compatible permission and attribution. You keep ownership of your contribution; no copyright assignment is requested.

Keep discussion respectful, specific and focused on the work. Maintainers may remove spam, personal attacks, confidential material and off-topic promotion.
