#!/usr/bin/env python3
"""
Shared Notion API client.

Provides authenticated HTTP requests and paginated database queries.
Used by all other notion modules.

Usage (CLI):
  python3 scripts/notion/notion_client.py --test
"""

import json
import os
import sys
import urllib.request

try:
    from .config import NOTION_TOKEN, NOTION_API
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from config import NOTION_TOKEN, NOTION_API


def notion_request(endpoint, method="POST", data=None):
    """Make an authenticated request to the Notion API.

    Args:
        endpoint: API path (e.g., "databases/{id}/query" or "pages/{id}")
        method: HTTP method (GET, POST, PATCH)
        data: Dict to send as JSON body (optional)

    Returns:
        Parsed JSON response dict.
    """
    if not NOTION_TOKEN:
        print("Error: NOTION_TOKEN environment variable not set.", file=sys.stderr)
        sys.exit(1)

    url = f"{NOTION_API}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    req = urllib.request.Request(url, method=method, headers=headers)
    if data:
        req.data = json.dumps(data).encode()

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(json.dumps({"success": False, "error": f"HTTP {e.code}: {body[:200]}"}), file=sys.stderr)
        sys.exit(1)


def notion_post(path, body=None):
    """Convenience alias for notion_request with POST method."""
    return notion_request(path, method="POST", data=body)


def load_all_rows(db_id, filter_body=None):
    """Load all rows from a Notion database, handling pagination.

    Args:
        db_id: Notion database ID
        filter_body: Optional filter dict for the query

    Returns:
        List of row dicts (Notion page objects).
    """
    rows = []
    cursor = None

    while True:
        body = {"page_size": 100}
        if filter_body:
            body["filter"] = filter_body
        if cursor:
            body["start_cursor"] = cursor

        data = notion_post(f"databases/{db_id}/query", body)
        rows.extend(data.get("results", []))

        if data.get("has_more"):
            cursor = data.get("next_cursor")
        else:
            break

    return rows


def main():
    if "--test" in sys.argv:
        if not NOTION_TOKEN:
            print("FAIL: NOTION_TOKEN not set")
            sys.exit(1)
        try:
            result = notion_request("users/me", method="GET")
            print(f"OK: Connected as {result.get('name', 'unknown')}")
        except SystemExit:
            print("FAIL: Could not connect to Notion API")
            sys.exit(1)
    else:
        print("Usage: python3 scripts/notion/notion_client.py --test")


if __name__ == "__main__":
    main()
