#!/usr/bin/env python3
"""
Companies Database — load companies from Notion by category.

Usage:
  python3 scripts/notion/db_companies.py --categories Dream Big-Tech
  python3 scripts/notion/db_companies.py --categories Startup --pretty
"""

import argparse
import json
import sys
import os

try:
    from .notion_client import load_all_rows
    from .config import NOTION_DB_COMPANIES
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from notion_client import load_all_rows
    from config import NOTION_DB_COMPANIES


def load_companies(categories):
    """Load companies from Notion, filtered by category.

    Args:
        categories: List of category names (e.g., ["Dream", "Big-Tech"])

    Returns:
        List of dicts: [{"name": str, "careers_url": str, "categories": [str]}]
    """
    category_filters = [
        {"property": "Category", "multi_select": {"contains": cat}}
        for cat in categories
    ]
    filter_body = {"or": category_filters} if len(category_filters) > 1 else category_filters[0]

    rows = load_all_rows(NOTION_DB_COMPANIES, filter_body)

    companies = []
    for row in rows:
        props = row.get("properties", {})
        name = "".join(t.get("plain_text", "") for t in props.get("Company", {}).get("title", [])).strip()
        careers_url = (props.get("Careers_Page", {}).get("url") or "").strip()
        cats = [c["name"] for c in props.get("Category", {}).get("multi_select", [])]

        if name and careers_url:
            companies.append({"name": name, "careers_url": careers_url, "categories": cats})

    return companies


def main():
    parser = argparse.ArgumentParser(description="Load companies from Notion.")
    parser.add_argument("--categories", nargs="+", default=["Dream", "Big-Tech"])
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    companies = load_companies(args.categories)

    if args.pretty:
        print(f"Found {len(companies)} companies (categories: {', '.join(args.categories)}):\n")
        for c in companies:
            print(f"  {c['name']:30s} | {str(c['categories']):30s} | {c['careers_url']}")
    else:
        print(json.dumps(companies, indent=2))


if __name__ == "__main__":
    main()
