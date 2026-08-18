# Repository Guidelines

## Project Structure & Module Organization

This repository contains small, standalone Python command-line utilities. Scripts live under `daily/`:

- `daily/time_check.py` calculates an expected departure time from an hour and minute.
- `daily/full_path.py` resolves a path, prints it, and copies it with an available system clipboard tool.

Keep each utility focused and independently executable. Place new recurring personal utilities in `daily/`; add a separate top-level directory only when a clearly different category emerges. Python cache files, virtual environments, coverage output, editor settings, and `.env` files are excluded through `.gitignore`.

## Build, Test, and Development Commands

The project has no build step or third-party runtime dependencies. Use Python 3 directly:

```sh
python3 daily/time_check.py 09:30
python3 daily/time_check.py 09:30 13:20-14:30
python3 daily/full_path.py ./daily
python3 -m py_compile daily/*.py
```

The first two commands exercise the current scripts. The compile command provides a quick syntax check. On macOS, `full_path.py` uses `pbcopy`; on other systems it looks for `wl-copy`, `xclip`, `xsel`, or `clip`.

## Coding Style & Naming Conventions

Follow standard Python conventions: four-space indentation, `snake_case` for modules and functions, and `UPPER_CASE` for constants. Include a Python 3 shebang for directly executable scripts. Prefer type annotations, `pathlib.Path` for filesystem paths, short docstrings for public functions, and an explicit `main() -> int` guarded by `if __name__ == "__main__"`. Keep dependencies in the standard library unless a strong need is documented.

## Testing Guidelines

No automated test suite is currently configured. For every change, run the syntax check and manually exercise normal and error paths. If tests are added, use `pytest`, store them in `tests/`, and name files `test_<script>.py`. Isolate time, filesystem, subprocess, and clipboard behavior so tests remain deterministic.

## Commit & Pull Request Guidelines

There is no existing commit history from which to infer conventions. Use short, imperative commit subjects, such as `Add argument validation to time check`. Keep commits scoped to one utility or concern. Pull requests should explain the behavior change, list commands used to verify it, link relevant issues, and include sample terminal output when command-line behavior changes. Never commit secrets or machine-specific configuration.
