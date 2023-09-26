install:
	chmod +x ./scripts/install.sh
	./scripts/install.sh

.PHONY: test
test:
	. .venv/bin/activate; python3 -m pytest test/**/*_test.py

analyze:
	. .venv/bin/activate; mypy src/ --strict

lint:
	. .venv/bin/activate; python3 -m ruff src/

test_ci:
	. .venv/bin/activate; python3 -m pytest test/**/*_test.py \
		--doctest-modules \
		--junitxml=reports/test-results-$(shell cat .python-version).xml

lint_ci:
	. .venv/bin/activate; python3 -m ruff check --format=github --target-version=py311 src/

deploy: install test_ci lint_ci analyze