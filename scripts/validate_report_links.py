#!/usr/bin/env python3
"""Validate evidence links in a generated Xiaohongshu HTML report."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlparse


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        self.links.append(dict(attrs))


def validate(path):
    html = path.read_text(encoding="utf-8")
    parser = LinkParser()
    parser.feed(html)
    errors = []
    external_count = 0

    unresolved = sorted(set(re.findall(r"\{\{[^{}]*URL[^{}]*\}\}", html)))
    if unresolved:
        errors.append("Unresolved URL placeholders: " + ", ".join(unresolved))

    for index, attrs in enumerate(parser.links, start=1):
        href = (attrs.get("href") or "").strip()
        if not href or href == "#":
            errors.append(f"Link {index} has an empty or placeholder href")
            continue
        parsed = urlparse(href)
        if parsed.scheme in {"http", "https"}:
            external_count += 1
            rel = set((attrs.get("rel") or "").split())
            if attrs.get("target") != "_blank":
                errors.append(f"External link {index} must use target=_blank: {href}")
            if not {"noopener", "noreferrer"}.issubset(rel):
                errors.append(f"External link {index} must use rel=noopener noreferrer: {href}")

    if external_count == 0:
        errors.append("No external evidence links found")
    return errors, external_count


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_report_links.py <report.html>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Report not found: {path}", file=sys.stderr)
        return 2
    errors, count = validate(path)
    if errors:
        print("Link validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Link validation passed: {count} external links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
