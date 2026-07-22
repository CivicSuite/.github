from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.images = []
        self.landmarks = []
        self.headings = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"])
        if tag == "img":
            self.images.append(values)
        if tag in {"header", "nav", "main", "footer"}:
            self.landmarks.append(tag)
        if tag in {"h1", "h2", "h3"}:
            self.headings.append(tag)
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


class PublicSiteContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = SITE / "index.html"
        cls.html = cls.html_path.read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)

    def test_required_public_artifacts_exist(self):
        required = [
            ROOT / "README.md",
            ROOT / "profile" / "README.md",
            ROOT / "docs" / "getting-started.md",
            ROOT / "docs" / "architecture.md",
            ROOT / "docs" / "project-status.md",
            SITE / "index.html",
            SITE / "styles.css",
            SITE / "assets" / "suite-architecture.svg",
            ROOT / ".github" / "workflows" / "pages.yml",
        ]
        self.assertEqual([], [str(path.relative_to(ROOT)) for path in required if not path.is_file()])

    def test_page_has_accessible_structure(self):
        self.assertIn("CivicSuite", self.parser.title)
        self.assertEqual(1, self.parser.headings.count("h1"))
        self.assertTrue({"header", "nav", "main", "footer"}.issubset(self.parser.landmarks))
        self.assertIn('href="#main"', self.html)
        self.assertRegex(self.html, r'<meta\s+name="description"\s+content="[^"]+"')
        self.assertRegex(self.html, r'<html\s+lang="en"')
        self.assertNotIn("TODO", self.html)

    def test_local_links_and_images_resolve(self):
        missing = []
        for href in self.parser.hrefs:
            if href.startswith(("https://", "mailto:", "#")):
                continue
            target = (SITE / href.split("#", 1)[0]).resolve()
            if not target.exists():
                missing.append(href)
        for image in self.parser.images:
            self.assertTrue(image.get("alt"), f"Image is missing alt text: {image}")
            target = (SITE / image["src"]).resolve()
            if not target.exists():
                missing.append(image["src"])
        self.assertEqual([], missing)

    def test_internal_anchors_resolve(self):
        anchors = [href[1:] for href in self.parser.hrefs if href.startswith("#")]
        self.assertEqual([], [anchor for anchor in anchors if anchor not in self.parser.ids])

    def test_civic_claims_include_status_and_human_review_guardrails(self):
        normalized = re.sub(r"\s+", " ", self.html).lower()
        self.assertIn("public beta", normalized)
        self.assertIn("not production-ready", normalized)
        self.assertIn("humans decide", normalized)
        self.assertIn("no cloud", normalized)
        self.assertIn("no telemetry", normalized)

    def test_css_includes_responsive_focus_and_reduced_motion_rules(self):
        css = (SITE / "styles.css").read_text(encoding="utf-8")
        self.assertIn("@media (max-width:", css)
        self.assertIn(":focus-visible", css)
        self.assertIn("prefers-reduced-motion", css)
        self.assertNotRegex(css, r"outline\s*:\s*(?:0|none)")


if __name__ == "__main__":
    unittest.main()
