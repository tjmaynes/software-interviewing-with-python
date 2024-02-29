install:
	chmod +x ./scripts/install.sh
	./scripts/install.sh

.PHONY: test
test:
	. .venv/bin/activate; python3 -m pytest test/**/*_test.py

analyze:
	. .venv/bin/activate; mypy src/ --strict

lint:
	. .venv/bin/activate; python3 -m ruff check src/

test_ci:
	. .venv/bin/activate; python3 -m pytest test/**/*_test.py \
		--doctest-modules \
		--junitxml=reports/test-results-$(shell cat .python-version).xml

lint_ci:
	. .venv/bin/activate; python3 -m ruff check --target-version=py311 src/

deploy: install test_ci lint_ci analyze