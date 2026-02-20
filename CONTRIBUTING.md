# Contributing

Thanks for contributing to this project.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
make install-locked
make install-hooks
```

## Local quality checklist

Before opening a pull request, run:

```bash
make ci-check
```

This verifies:

- lockfile consistency (`make check-lock`)
- linting (`make lint`)
- tests with coverage (`make test`)

## Dependency changes

If you update `pyproject.toml` dependencies, regenerate the lockfile:

```bash
make lock
```

Commit both `pyproject.toml` and `requirements-dev.txt` together.

## Pull request expectations

- Keep PR scope focused and small
- Add or update tests when behavior changes
- Update README or docs for user-facing changes
- Ensure CI is green before requesting review
