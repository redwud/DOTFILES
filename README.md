# DOTFILES

DOTFILES is a personal collection of small command-line utilities. Despite the name, this repository is not limited to traditional shell dotfiles; the name is retained simply because it is how the collection is known.

## Requirements

- Python 3
- A supported clipboard command for `full_path.py`: `pbcopy`, `wl-copy`, `xclip`, `xsel`, or `clip`

The scripts use only the Python standard library, so no package installation is required.

## Utilities

### Time check

`daily/time_check.py` calculates when a work period ends. The base duration is 8 hours and 47 minutes.

Pass the starting time in zero-padded, 24-hour `HH:MM` format:

```sh
python3 daily/time_check.py 09:30
```

Optionally provide one same-day out-of-office range. Its duration is added to the base work period:

```sh
python3 daily/time_check.py 09:30 13:20-14:30
```

In this example, the 1-hour-10-minute absence moves the expected end time from `18:17` to `19:27`. The range must be increasing and use `HH:MM-HH:MM` format.

### Full path

`daily/full_path.py` resolves a relative or absolute path, prints the result, and copies it to the system clipboard:

```sh
python3 daily/full_path.py ./daily
```

If no path is supplied, the current directory is used. The resolved path is still printed if no supported clipboard utility is available, but the script exits with an error status.

## Development

Run a quick syntax check for all scripts with:

```sh
python3 -m py_compile daily/*.py
```

See [AGENTS.md](AGENTS.md) for repository structure, coding conventions, testing expectations, and contribution guidelines.
