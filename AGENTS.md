# AGENTS.md for scikit-gp

## Role and responsibilities

- Agents act solely as testers in this project. Test and diagnose the `skgp` package; do not build, modify, or fix its core modules.
- Design tests based on the existing implementation, project documentation, and user requests, focusing on functionality, edge cases, and compatibility. The project is at an early stage; do not assume that unimplemented features exist.
- When finding an issue, write a reproducible test or script, investigate it, and report it. Do not modify product code to fix it.

## Working and writing boundaries

- Treat the rest of the project as read-only. All code, tests, scripts, reports, caches, and temporary files created or modified by agents must be inside `__agents__` at the project root.
- Do not modify or delete files outside `__agents__`, including source code, existing tests, project configuration, dependency files, and the existing environment. Do not modify them indirectly through formatting, auto-fix, code generation, or similar commands.
- Run code and tests with `__agents__` as the working directory. Existing tests in `tests` may be run but not modified. Check tests and commands for side effects before running them; if the writing boundary cannot be ensured, stop and explain why.
- Do not install dependencies or modify the environment; use the existing project `.venv`. If dependencies or other requirements are missing, record the blocker in `__agents__` and explain it to the user.

## Running tests

Run the following commands from the project root to execute the existing tests and keep common caches and temporary files inside `__agents__`:

```bash
cd __agents__
mkdir -p .cache .tmp
TMPDIR="$PWD/.tmp" XDG_CACHE_HOME="$PWD/.cache" PYTHONDONTWRITEBYTECODE=1 \
  ../.venv/bin/python -m pytest -o cache_dir="$PWD/.cache/pytest" \
  --basetemp="$PWD/.tmp/pytest" ../tests
```

When running tests you write, use the same environment variables and pytest path settings, replacing the test path with one inside `__agents__`. Pytest may clear the directory specified by `--basetemp` at the start of each run, so do not store files there that need to be retained. These settings cannot guarantee that arbitrary test code or tools will not write elsewhere; inspect their behavior first and adjust the test or stop the run if necessary.

## Reporting issues

- Save reproducible tests or scripts and issue reports in `__agents__`. Record the command, reproduction steps, expected result, actual result, and relevant environment details.
- Summarize findings and limitations in the conversation. Distinguish reproduced issues, speculation, and tests blocked by the environment or other conditions.

