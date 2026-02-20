.PHONY: help install install-locked install-hooks lock check-lock format lint test ci-check demo notebook clean

PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python)

help:
	@echo "Available targets:"
	@echo "  install         - install project + dev dependencies"
	@echo "  install-locked  - install from pinned lockfile"
	@echo "  install-hooks   - install pre-commit hooks"
	@echo "  lock            - regenerate requirements-dev.txt"
	@echo "  check-lock      - verify requirements-dev.txt is up to date"
	@echo "  format          - auto-format imports and code with Ruff"
	@echo "  lint            - run static lint checks"
	@echo "  test            - run unit tests with coverage"
	@echo "  ci-check        - run lock check, lint, and tests"
	@echo "  demo            - run package demo script"
	@echo "  notebook        - open analysis notebook/script in Jupyter Lab"
	@echo "  clean           - remove common caches/build artifacts"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .[dev]

install-locked:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements-dev.txt
	$(PYTHON) -m pip install -e . --no-deps

install-hooks:
	$(PYTHON) -m pre_commit install

lock:
	$(PYTHON) -m piptools compile --strip-extras pyproject.toml --extra dev -o requirements-dev.txt

check-lock:
	$(PYTHON) -m piptools compile --strip-extras pyproject.toml --extra dev -o requirements-dev.txt
	git diff --exit-code -- requirements-dev.txt

format:
	$(PYTHON) -m ruff check . --fix
	$(PYTHON) -m ruff format .

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest -q --cov=social_network_graph_system --cov-report=term-missing

ci-check:
	$(MAKE) check-lock
	$(MAKE) lint
	$(MAKE) test

demo:
	$(PYTHON) -m social_network_graph_system.demo

notebook:
	$(PYTHON) -m jupyter lab notebooks/social_network_graph_analysis.py

clean:
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov build dist *.egg-info
