# Contributing

This repository owns CivicSuite's organization profile and organization-level landing page. Product behavior, installer details, module documentation, architecture decisions, and current status belong in the [`civicsuite` umbrella repository](https://github.com/CivicSuite/civicsuite) or the relevant module repository.

## Make a profile or landing-page change

1. Create a topic branch.
2. Update `profile/README.md`, `site/`, or the concise routing documents in `docs/`.
3. Confirm every changing product claim against the umbrella repository.
4. Run `python -m unittest discover -s tests -v`.
5. Preview with `python -m http.server 4173 --directory site` at desktop and mobile widths.
6. Open a pull request that identifies the authoritative source for any changed version, status, requirement, or maturity claim.

For product contributions, bug routing, and security reporting, use the [suite contribution guide](https://github.com/CivicSuite/civicsuite/blob/main/CONTRIBUTING.md).
