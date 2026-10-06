# Security and private information

Do not publish credentials, customer telemetry, raw vendor submissions, recordings or personal information in issues, discussions or pull requests.

For a security concern or accidental disclosure, use [GitHub's private vulnerability reporting](https://github.com/secops-unpacked/asef/security/advisories/new), enabled for this repository. Reports are visible to repository maintainers, not public issues. Include only the minimum information needed to reproduce the concern; never include live secrets or customer evidence.

This repository contains documentation, data and offline reference tooling. It does not contain the hosted platform's API, authentication or database. A platform vulnerability should be reported privately to the platform maintainer, not filed publicly as a framework correction.

Maintainers should review unexpected files and generated output before merging. Automated checks are useful, but they are not a complete secret detector or a security audit.
