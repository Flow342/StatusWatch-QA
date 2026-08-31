# StatusWatch-QA

Automated tests for the StatusWatch service. API tests built with pytest and requests.

## Requirements

- Python 3.12+
- A running StatusWatch instance (defaults to `http://localhost:4000`)

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Copy the example config and fill in your own values:

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `URL` | Base URL of the service |
| `ADMIN_USERNAME` | Admin login |
| `ADMIN_PASSWORD` | Admin password |

`.env` is not tracked by git.

## Running

All tests:

```bash
pytest
```

By marker:

```bash
pytest -m smoke
```

A single file:

```bash
pytest tests/api/test_endpoints.py
```

Available markers: `smoke`, `regression`.

## Layout

```
conftest.py              shared fixtures
pyproject.toml           pytest settings
tests/api/               API tests
```

## Tests

| Test | Marker | Checks |
|---|---|---|
| `test_health_check` | smoke | `GET /api/health` returns 200 |
