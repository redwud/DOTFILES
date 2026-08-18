#!/usr/bin/env python3
"""Print a path as an absolute path and copy it to the clipboard."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def copy_to_clipboard(text: str) -> None:
    """Copy text with the first supported system clipboard command."""
    clipboard_commands = (
        ("pbcopy",),
        ("wl-copy",),
        ("xclip", "-selection", "clipboard"),
        ("xsel", "--clipboard", "--input"),
        ("clip",),
    )

    for command in clipboard_commands:
        if shutil.which(command[0]):
            subprocess.run(command, input=text, text=True, check=True)
            return

    raise RuntimeError(
        "No supported clipboard utility found "
        "(tried pbcopy, wl-copy, xclip, xsel, and clip)."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Display a full path and copy it to the clipboard."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="relative or absolute path (default: current working directory)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    full_path = str(Path(args.path).expanduser().resolve(strict=False))

    print(full_path, flush=True)
    try:
        copy_to_clipboard(full_path)
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Could not copy path to clipboard: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
