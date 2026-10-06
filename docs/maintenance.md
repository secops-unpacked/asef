# Maintaining the public framework

## Sources and version boundaries

The initial repository was prepared from the updated ASEF document and selected framework definitions at source revision `19aeccd34783dd733561e1cfd4694b922b4e7506`.

`data/manifest.json` records three different things:

- `frameworkVersion`: the methodology baseline, currently 3.1.3.
- `publicationRevision`: this public documentation/catalogue revision, currently 2026-10-06.1.
- `schemaVersion`: the public JSON format, currently 1.

These are not interchangeable. A documentation clarification is not automatically a new application scoring engine. The reference scripts demonstrate current ASEF 3 calculations; they do not implement historical ASEF 2 or import application backups.

## A controlled update process

1. Discuss substantive methodology changes in an issue or discussion.
2. Update the relevant Markdown and JSON, preserving stable IDs and identifying changed meanings.
3. Update examples, tests and the changelog. Record migration consequences.
4. Run validation and tests; review the diff for private content and unintended files.
5. Obtain maintainer approval and merge the pull request.
6. Publish a versioned reference when ready. Do not retag an existing release.
7. Separately implement/deploy approved application changes, then reconcile the platform guide and Google Doc with the published method.

There is no automatic synchronization in this first version. Do not edit three independent “official” versions and assume they remain aligned. A draft in Google Docs does not override a released reference; a repository merge does not prove the application has been deployed.

## Catalogue updates

The JSON is a curated public snapshot, not a live export of the database. Review changes deliberately. Exclude retired Builder reference scores, private data and operational configuration. Keep `sourceZone` for compatibility and current `shiftMapStages` guidance separate.

Broad RFI criteria must not be expanded into detailed capability scores automatically. Future additions should include definitions, exclusions, examples, and migration notes for older evaluations. Known differences are documented in [catalogue boundaries](catalogue.md).

## Repository controls

- Keep Issues enabled and Discussions available for methodology questions.
- Use pull requests after this initial publication.
- Enable branch protection or repository rules requiring review and the validation check. CODEOWNERS alone does not enforce this.
- Keep workflow permissions read-only and avoid `pull_request_target` for running contributed code.
- Pin third-party Actions by commit; review updates before changing pins.
- No secrets or database access are required by the reference tooling.
- Keep vendor-profile publication and consent in the application, not public GitHub issues.

## Release checklist

- [ ] Version metadata and changelog agree.
- [ ] Definitions, examples and calculations agree.
- [ ] Technology and MDR remain separate.
- [ ] Historical IDs and evaluation meaning are preserved or explicitly migrated.
- [ ] Validation and tests pass.
- [ ] All added files have been reviewed for confidential information and reuse rights.
- [ ] Public links work, contribution forms are visible, and license attribution is intact.
- [ ] Any required platform/doc synchronization is explicitly tracked, not assumed complete.
