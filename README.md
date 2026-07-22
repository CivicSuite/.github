# CivicSuite organization profile and public front door

This repository owns CivicSuite's GitHub organization profile, concise public documentation, and the source for an organization-level landing page. Detailed product documentation and the current Windows Local release remain authoritative in the [`CivicSuite/civicsuite`](https://github.com/CivicSuite/civicsuite) umbrella repository.

## Public surfaces

- [`profile/README.md`](profile/README.md) — the profile displayed on the CivicSuite organization page.
- [`site/`](site/) — dependency-free static landing page source.
- [`docs/getting-started.md`](docs/getting-started.md) — visitor and evaluator routing.
- [`docs/architecture.md`](docs/architecture.md) — concise suite architecture overview.
- [`docs/project-status.md`](docs/project-status.md) — public maturity language and source-of-truth links.

The detailed product site is live at <https://civicsuite.github.io/civicsuite/>. This repository's site is an organization hub and does not replace that product documentation.

## Preview the landing page

No package installation or build step is required.

```powershell
python -m http.server 4173 --directory site
```

Open <http://localhost:4173>. To verify the repository contract:

```powershell
python -m unittest discover -s tests -v
```

## Deployment

The Pages workflow publishes the contents of `site/` as a static artifact after changes land on `main`. A repository administrator must select **GitHub Actions** as the Pages source before the first deployment. See [`docs/deployment.md`](docs/deployment.md).

## Content authority

Public status, versions, release evidence, checksums, requirements, and module maturity must be sourced from the umbrella repository. Do not duplicate fast-changing details here unless they are accompanied by a verification date and an authoritative link.

## License

Documentation and site content are licensed under [CC BY 4.0](LICENSE). Code snippets, tests, and workflow configuration are licensed under [Apache License 2.0](LICENSE-CODE).
