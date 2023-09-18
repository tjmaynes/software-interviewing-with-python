install:
	chmod +x ./scripts/install.sh
	./scripts/install.sh

test:
	. .venv/bin/activate; python3 -m pytest

deploy: install test