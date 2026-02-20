# Social Network Graph System

[![CI](https://github.com/anneliset47/social-network-graph-system/actions/workflows/ci.yml/badge.svg)](https://github.com/anneliset47/social-network-graph-system/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![Status](https://img.shields.io/badge/status-actively%20maintained-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-97%25-success)

Production-style Python project demonstrating graph data structures, BFS traversal, and simple recommendation scoring on a social network.

## Highlights

- Clean `src/` package layout with typed core graph API
- Deterministic sample data powering both tests and demo
- Reproducible workflow (`requirements-dev.txt`, `Makefile`, pre-commit, CI)
- Verified quality gates (`make ci-check`)

## What this demonstrates

- Graph modeling using adjacency lists and hash maps
- Exact-degree reachability via breadth-first search (BFS)
- Interest-based recommendation scoring for non-connected users
- Reproducible engineering workflow (lockfile + Makefile + pre-commit + CI)
- Technical communication with notebook analysis and written report

## Repository layout

```text
social-network-graph-system/
├── .github/workflows/ci.yml
├── data/
├── notebooks/
│   └── social_network_graph_analysis.py
├── report/
│   └── social_network_graph_report.pdf
├── src/social_network_graph_system/
│   ├── demo.py
│   ├── graph.py
│   └── sample_data.py
├── tests/
│   └── test_graph.py
├── Makefile
├── pyproject.toml
└── requirements-dev.txt
```

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
make install-locked
make ci-check
make demo
```

## Developer workflow

- `make help` — list all available tasks
- `make format` — auto-fix lint and format issues
- `make lint` — run Ruff checks
- `make test` — run tests with coverage
- `make ci-check` — run lockfile, lint, and tests
- `make notebook` — open analysis script in Jupyter Lab
- `make install-hooks` — install pre-commit hooks

## Core API

Main class: `SocialGraph` (`src/social_network_graph_system/graph.py`)

- `first_degree_connections(user_id)`
- `connections_at_degree(user_id, degree)`
- `second_degree_connections(user_id)`
- `third_degree_connections(user_id)`
- `suggest_connections_based_on_interests()`

## Reproducibility guarantees

- Pinned tool and dependency lockfile in `requirements-dev.txt`
- Deterministic sample data shared by demo and tests
- CI on push/pull request for Python 3.11 and 3.12
- Local quality gates mirrored from CI (`make ci-check`)

## Recruiter summary

- **Algorithms:** graph traversal, shortest-path distance layering, similarity scoring
- **Engineering:** package layout (`src/`), automated quality checks, reproducible setup
- **Communication:** accompanying analysis notebook script and formal report PDF

## Next enhancements

- Weighted recommendation ranking (mutual friends + preference overlap)
- Graph visualization for network exploration
- Synthetic-data benchmark for scale testing
