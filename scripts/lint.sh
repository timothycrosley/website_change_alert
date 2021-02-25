#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports website_change_alert/
poetry run isort --check --diff website_change_alert/ tests/
poetry run black --check website_change_alert/ tests/
poetry run flake8 website_change_alert/ tests/
poetry run safety check -i 39462
poetry run bandit -r website_change_alert/
