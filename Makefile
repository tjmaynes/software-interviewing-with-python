install:
	chmod +x ./scripts/install.sh
	./scripts/install.sh

test:
	. .venv/bin/activate; python3 -m pytest **/*_test.py

analyze:
	. .venv/bin/activate; mypy \
		data_structures/ \
		--strict

lint:
	. .venv/bin/activate; python3 -m ruff .

test_ci:
	. .venv/bin/activate; python3 -m pytest **/*_test.py \
		--doctest-modules \
		--junitxml=reports/test-results-$(shell cat .python-version).xml

lint_ci:
	. .venv/bin/activate; python3 -m ruff check --format=github --target-version=py311 .

deploy: install test_ci lint_ci analyze