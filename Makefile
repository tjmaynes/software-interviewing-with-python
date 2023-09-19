install:
	chmod +x ./scripts/install.sh
	./scripts/install.sh

test:
	. .venv/bin/activate; python3 -m pytest

lint:
	. .venv/bin/activate; python3 -m ruff --format=github --target-version=py311 .

lint_ci:
	. .venv/bin/activate; python3 -m ruff check --format=github --target-version=py311 .

deploy: install test lint_ci