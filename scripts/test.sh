#!/bin/bash
set -euxo pipefail

./scripts/lint.sh
poetry run pytest -s --cov=website_change_alert/ --cov=tests --cov-report=term-missing ${@-} --cov-report html
