# Landing-page deployment

The organization hub is a dependency-free static site in `site/`. The workflow at `.github/workflows/pages.yml` uploads that directory directly to GitHub Pages.

## First deployment

1. In the `.github` repository, open **Settings → Pages**.
2. Under **Build and deployment**, choose **GitHub Actions** as the source.
3. Merge or push the site changes to `main`.
4. Watch the **Deploy organization landing page** workflow.
5. Add the resulting URL to the repository homepage only after the successful deployment confirms it.

GitHub Pages determines the final project URL. Do not publish or document a guessed URL before that first successful deployment.

## Local preview

```powershell
python -m http.server 4173 --directory site
```

The site uses only relative asset URLs and in-page anchors, so it remains portable under a repository subpath.

## Verification

```powershell
python -m unittest discover -s tests -v
```

The contract test checks required artifacts, semantic structure, internal anchors, local assets, status guardrails, responsive CSS, focus treatment, and reduced-motion support.
