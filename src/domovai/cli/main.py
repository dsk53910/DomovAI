from __future__ import annotations

import argparse
from typing import Sequence

from importlib.metadata import PackageNotFoundError, version

from domovai import __version__


def get_version() -> str:
    try:
        return version("domovai")
    except PackageNotFoundError:
        return __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="domovai",
        description="Domovai CLI (PoC v0.1)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"domovai {get_version()}",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Index a Java repository")
    index_parser.add_argument("path", help="Path to a Java repository")

    search_parser = subparsers.add_parser("search", help="Semantic search over indexed code")
    search_parser.add_argument("query", help="Search query")

    explain_parser = subparsers.add_parser("explain", help="Explain a symbol or component")
    explain_parser.add_argument("target", help="Symbol or component name")

    subparsers.add_parser("stats", help="Show index statistics")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "index":
        print(f"Indexing: {args.path}")
    elif args.command == "search":
        print(f"Searching: {args.query}")
    elif args.command == "explain":
        print(f"Explaining: {args.target}")
    elif args.command == "stats":
        print("Stats: not implemented yet.")
    else:
        parser.error(f"Unknown command: {args.command}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
