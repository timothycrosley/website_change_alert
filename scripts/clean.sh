#!/bin/bash
set -euxo pipefail

poetry run isort website_change_alert/ tests/
poetry run black website_change_alert/ tests/
