#!/usr/bin/env python3
"""
Preferences Page — load job search preferences from Notion.

Fetches the Profile/Preferences page once and extracts sections by header.

Usage:
  python3 scripts/notion/page_preferences.py --title-filter [--pretty]
  python3 scripts/notion/page_preferences.py --search-queries [--pretty]
  python3 scripts/notion/page_preferences.py --target-roles [--pretty]
  python3 scripts/notion/page_preferences.py --adaptive-framing [--pretty]
  python3 scripts/notion/page_preferences.py --exit-narrative [--pretty]
  python3 scripts/notion/page_preferences.py --cross-cutting [--pretty]
  python3 scripts/notion/page_preferences.py --portfolio [--pretty]
  python3 scripts/notion/page_preferences.py --compensation [--pretty]
  python3 scripts/notion/page_preferences.py --negotiation [--pretty]
  python3 scripts/notion/page_preferences.py --location [--pretty]
  python3 scripts/notion/page_preferences.py --user-input-jobs [--pretty]
  python3 scripts/notion/page_preferences.py --all
"""

import json
import os
import re
import sys

try:
    from .page_reader import fetch_page
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from page_reader import fetch_page

# config is loaded by page_reader → no need to import here

_cached_text = None


def _fetch_page():
    """Fetch the Notion Preferences page (cached within process)."""
    global _cached_text
    if _cached_text is not None:
        return _cached_text

    try:
        _cached_text = fetch_page("profile")
    except Exception as e:
        print(f"Error fetching Notion Preferences: {e}", file=sys.stderr)
        _cached_text = ""

    return _cached_text


def _extract_code_block(text, header):
    """Extract content from a ```python/markdown code block under a # header."""
    pattern = rf"# {re.escape(header)}\n```(?:python|markdown)?\n(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1) if match else ""


def _extract_section(text, header):
    """Extract all text between a # header and the next # header."""
    pattern = rf"# {re.escape(header)}\n(.*?)(?=\n# |\Z)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


# ── Loaders ─────────────────────────────────────────────────────────

def load_title_filter():
    """Load positive and negative title filter keywords."""
    text = _fetch_page()

    def extract_keywords(header):
        block = _extract_code_block(text, header)
        return [m.group(1) for m in re.finditer(r'"([^"]+)"', block)]

    return {
        "positive": extract_keywords("Positive Job Title Filters"),
        "negative": extract_keywords("Negative Job Title Filters"),
    }


def load_search_queries():
    """Load WebSearch queries for broad job discovery."""
    text = _fetch_page()
    block = _extract_code_block(text, "Job Board Search Queries")

    queries = []
    for m in re.finditer(r"-\s*name:\s*(.+?)\n\s+query:\s*'([^']+)'", block):
        queries.append({"name": m.group(1).strip(), "query": m.group(2).strip()})
    return queries


def load_target_roles():
    return _extract_section(_fetch_page(), "Target Roles")

def load_adaptive_framing():
    return _extract_section(_fetch_page(), "Adaptive Framing")

def load_exit_narrative():
    return _extract_section(_fetch_page(), "Exit Narrative")

def load_cross_cutting():
    return _extract_section(_fetch_page(), "Cross Cutting Advantage")

def load_portfolio():
    return _extract_section(_fetch_page(), "Portfolio")

def load_compensation():
    return _extract_section(_fetch_page(), "Target Compensation")

def load_negotiation():
    return _extract_section(_fetch_page(), "Negotiation Scripts")

def load_location():
    return _extract_section(_fetch_page(), "Location Policy")

def load_user_input_jobs():
    return _extract_section(_fetch_page(), "User Input Jobs")


# ── Title filter builder ────────────────────────────────────────────

def _build_positive_matcher(keyword):
    """Build a matcher for a positive keyword.

    Short keywords (≤3 chars like AI, ML, NLP, RAG) use word boundary regex
    to avoid false matches (e.g., "AI" matching "Chair", "ML" matching "HTML").
    Longer keywords use substring match.
    """
    kw_lower = keyword.lower()
    if len(kw_lower) <= 3:
        pattern = re.compile(r"\b" + re.escape(kw_lower) + r"\b", re.IGNORECASE)
        return lambda title: bool(pattern.search(title))
    else:
        return lambda title: kw_lower in title.lower()


def build_title_filter(title_filter_config=None):
    """Build a title filter function.

    Positive keywords: word boundary regex for short keywords (≤3 chars),
    substring match for longer phrases. At least 1 must match.

    Negative keywords: always substring match. 0 must match.

    Args:
        title_filter_config: Dict with "positive" and "negative" keyword lists.
                             If None, loads from Notion Preferences page.

    Returns:
        A function that takes a title string and returns True if it passes.
    """
    if title_filter_config is None:
        title_filter_config = load_title_filter()

    positive_matchers = [_build_positive_matcher(k) for k in title_filter_config.get("positive", [])]
    negative = [k.lower() for k in title_filter_config.get("negative", [])]

    print(f"  Title filter: {len(positive_matchers)} positive, {len(negative)} negative keywords")

    def matches(title):
        lower = title.lower()
        has_positive = len(positive_matchers) == 0 or any(m(title) for m in positive_matchers)
        has_negative = any(k in lower for k in negative)
        return has_positive and not has_negative

    return matches


def load_all():
    """Load all preferences in one call."""
    return {
        "title_filter": load_title_filter(),
        "search_queries": load_search_queries(),
        "target_roles": load_target_roles(),
        "adaptive_framing": load_adaptive_framing(),
        "exit_narrative": load_exit_narrative(),
        "cross_cutting": load_cross_cutting(),
        "portfolio": load_portfolio(),
        "compensation": load_compensation(),
        "negotiation": load_negotiation(),
        "location": load_location(),
        "user_input_jobs": load_user_input_jobs(),
    }


# ── CLI ─────────────────────────────────────────────────────────────

COMMANDS = {
    "--title-filter": ("Title Filter", load_title_filter),
    "--search-queries": ("Search Queries", load_search_queries),
    "--target-roles": ("Target Roles", load_target_roles),
    "--adaptive-framing": ("Adaptive Framing", load_adaptive_framing),
    "--exit-narrative": ("Exit Narrative", load_exit_narrative),
    "--cross-cutting": ("Cross Cutting Advantage", load_cross_cutting),
    "--portfolio": ("Portfolio", load_portfolio),
    "--compensation": ("Target Compensation", load_compensation),
    "--negotiation": ("Negotiation Scripts", load_negotiation),
    "--location": ("Location Policy", load_location),
    "--user-input-jobs": ("User Input Jobs", load_user_input_jobs),
}


def main():
    args = sys.argv[1:]
    pretty = "--pretty" in args

    if not args or "--help" in args:
        print("Usage: python3 scripts/notion/page_preferences.py <command> [--pretty]", file=sys.stderr)
        print("\nCommands:", file=sys.stderr)
        for flag, (label, _) in COMMANDS.items():
            print(f"  {flag:25s} {label}", file=sys.stderr)
        print(f"  {'--all':25s} Everything", file=sys.stderr)
        sys.exit(1)

    if "--all" in args:
        print(json.dumps(load_all(), indent=2, default=str))
        return

    for flag in args:
        if flag == "--pretty":
            continue
        if flag not in COMMANDS:
            continue

        label, loader = COMMANDS[flag]
        data = loader()

        if pretty:
            print(f"=== {label} ===\n")
            if isinstance(data, dict) and "positive" in data:
                print(f"Positive ({len(data['positive'])}):")
                for k in data["positive"]:
                    print(f"  + {k}")
                print(f"\nNegative ({len(data['negative'])}):")
                for k in data["negative"]:
                    print(f"  - {k}")
            elif isinstance(data, list):
                for i, item in enumerate(data, 1):
                    if isinstance(item, dict):
                        print(f"  {i:2d}. {item.get('name', '')}")
                        print(f"      {item.get('query', '')}")
                    else:
                        print(f"  {i}. {item}")
                    print()
            else:
                print(data)
            print()
        else:
            print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
