#!/usr/bin/env python3
"""
SQLGlot transpiler script for Emacs integration.

This script provides a command-line interface for SQLGlot operations
including transpilation between dialects and SQL formatting.
"""

import sys
import argparse
import json
from typing import Optional


DIALECTS_MAP: dict[str, str] = {}
try:
    import sqlglot
    from sqlglot import dialects

    DIALECTS_MAP = dialects.MODULE_BY_DIALECT
except ImportError:
    print(
        "Error: sqlglot package not installed. Run: python -m pip install sqlglot",
        file=sys.stderr,
    )
    sys.exit(1)


def transpile_sql(
    sql: str,
    read_dialect: Optional[str],
    write_dialect: Optional[str],
    identify: bool = False,
    pretty: bool = False,
) -> str:
    """Transpile SQL from one dialect to another with optional pretty printing."""
    try:
        if read_dialect is not None:
            read_dialect = DIALECTS_MAP[read_dialect]
        if write_dialect is not None:
            write_dialect = DIALECTS_MAP[write_dialect]
        result: list[str] = sqlglot.transpile(
            sql,
            read=read_dialect,
            write=write_dialect,
            identify=identify,
            pretty=pretty,
            pad=4,  # TODO: make it configurable
            indent=4,  # TODO: make it configurable
        )
        if result:
            return result[0]
        else:
            raise ValueError("No result from transpilation")
    except KeyError as e:
        raise RuntimeError(f"Unknown dialect: {e}")
    except Exception as e:
        operation: str = "formatting" if pretty else "transpilation"
        raise RuntimeError(f"SQL {operation} failed: {e}")


def get_version() -> str:
    """Get SQLGlot version."""
    return getattr(sqlglot, "__version__", "unknown")


def list_dialects() -> list[str]:
    """List all supported dialects."""
    return sorted(DIALECTS_MAP.keys())


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="SQLGlot transpiler for Emacs integration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Transpile command
    transpile_parser = subparsers.add_parser(
        "transpile", help="Transpile SQL between dialects"
    )
    transpile_parser.add_argument("--read", help="Read dialect (optional)")
    transpile_parser.add_argument("--write", help="Write dialect (optional)")
    transpile_parser.add_argument(
        "--identify", action="store_true", help="Preserve SQL formatting and casing"
    )
    transpile_parser.add_argument(
        "--sql", help="SQL to transpile (if not provided, reads from stdin)"
    )

    # Format command
    format_parser = subparsers.add_parser("format", help="Format/pretty-print SQL")
    format_parser.add_argument("--read", help="Read dialect (optional)")
    format_parser.add_argument("--write", help="Write dialect (optional)")
    format_parser.add_argument(
        "--identify", action="store_true", help="Preserve SQL formatting and casing"
    )
    format_parser.add_argument(
        "--sql", help="SQL to format (if not provided, reads from stdin)"
    )

    # Version command
    subparsers.add_parser("version", help="Show SQLGlot version")

    # Dialects command
    subparsers.add_parser("dialects", help="List supported dialects")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "version":
            print(get_version())

        elif args.command == "dialects":
            dialects: list[str] = list_dialects()
            print(json.dumps(dialects, indent=2))

        elif args.command in ["transpile", "format"]:
            sql: str = args.sql or sys.stdin.read()

            if not sql.strip():
                print("Error: No SQL provided", file=sys.stderr)
                sys.exit(1)

            pretty: bool = args.command == "format"
            result: str = transpile_sql(
                sql,
                args.read,
                args.write,
                identify=args.identify,
                pretty=pretty,
            )
            print(result, end="")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
