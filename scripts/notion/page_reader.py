#!/usr/bin/env python3
"""
Fetch Notion pages and convert blocks to readable markdown text.

Supports named projects (roma, sera, etc.), the profile/preferences page,
resume, and any arbitrary page ID.

Usage:
  python3 scripts/notion/page_reader.py roma
  python3 scripts/notion/page_reader.py profile
  python3 scripts/notion/page_reader.py <page_id>
  python3 scripts/notion/page_reader.py list
  python3 scripts/notion/page_reader.py all
"""

import json
import os
import sys
import urllib.request

try:
    from .config import NOTION_TOKEN, NOTION_API, PROJECTS, PARENT_PAGE
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from config import NOTION_TOKEN, NOTION_API, PROJECTS, PARENT_PAGE


def fetch_blocks(page_id, token=None):
    """Fetch all blocks from a Notion page."""
    token = token or NOTION_TOKEN
    if not token:
        print("Error: NOTION_TOKEN not set.", file=sys.stderr)
        sys.exit(1)

    url = f"{NOTION_API}/blocks/{page_id}/children?page_size=100"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def blocks_to_text(data):
    """Convert Notion blocks to readable markdown-like text."""
    lines = []
    for block in data.get("results", []):
        btype = block.get("type", "")

        if btype in ("heading_1", "heading_2", "heading_3"):
            text = "".join(t.get("plain_text", "") for t in block[btype].get("rich_text", []))
            level = int(btype[-1])
            lines.append(f"{'#' * level} {text}")
        elif btype == "paragraph":
            text = "".join(t.get("plain_text", "") for t in block["paragraph"].get("rich_text", []))
            if text:
                lines.append(text)
        elif btype == "bulleted_list_item":
            text = "".join(t.get("plain_text", "") for t in block["bulleted_list_item"].get("rich_text", []))
            lines.append(f"  - {text}")
        elif btype == "numbered_list_item":
            text = "".join(t.get("plain_text", "") for t in block["numbered_list_item"].get("rich_text", []))
            lines.append(f"  1. {text}")
        elif btype == "code":
            text = "".join(t.get("plain_text", "") for t in block["code"].get("rich_text", []))
            lang = block["code"].get("language", "")
            lines.append(f"```{lang}\n{text}\n```")
        elif btype == "divider":
            lines.append("---")
        elif btype == "toggle":
            text = "".join(t.get("plain_text", "") for t in block["toggle"].get("rich_text", []))
            lines.append(f"> {text}")
        elif btype == "child_page":
            lines.append(f"[Child Page: {block['child_page'].get('title', '')}]")
        elif btype == "callout":
            text = "".join(t.get("plain_text", "") for t in block["callout"].get("rich_text", []))
            lines.append(f"> {text}")
        elif btype == "quote":
            text = "".join(t.get("plain_text", "") for t in block["quote"].get("rich_text", []))
            lines.append(f"> {text}")
        elif btype == "to_do":
            text = "".join(t.get("plain_text", "") for t in block["to_do"].get("rich_text", []))
            checked = block["to_do"].get("checked", False)
            lines.append(f"  [{'x' if checked else ' '}] {text}")

    return "\n".join(lines)


def fetch_page(name_or_id):
    """Fetch a page by name or ID and return as markdown text.

    Args:
        name_or_id: A project name (e.g., "roma") or a Notion page ID.

    Returns:
        String of markdown-formatted page content.
    """
    name_lower = name_or_id.lower().strip()
    if name_lower in PROJECTS:
        page_id = PROJECTS[name_lower]
    elif len(name_lower) == 36 and "-" in name_lower:
        page_id = name_lower
    else:
        raise ValueError(f"Unknown project: {name_or_id}. Available: {', '.join(PROJECTS.keys())}")

    data = fetch_blocks(page_id)
    return blocks_to_text(data)


def list_projects():
    """List all available projects."""
    print("Available projects:")
    for name, pid in PROJECTS.items():
        print(f"  {name:20s} → {pid}")


def main():
    if len(sys.argv) < 2:
        list_projects()
        sys.exit(0)

    arg = sys.argv[1].lower().strip()

    if arg == "list":
        list_projects()
    elif arg == "all":
        for name, pid in PROJECTS.items():
            print(f"\n{'=' * 60}")
            print(f"PROJECT: {name.upper()}")
            print(f"{'=' * 60}\n")
            print(fetch_page(name))
    else:
        try:
            print(fetch_page(arg))
        except ValueError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
