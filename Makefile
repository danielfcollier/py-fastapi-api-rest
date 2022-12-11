run:
	@uvicorn main:app --reload

venv:
	@echo "run with: source .venv/bin/activate"
	@echo "stop with: deactivate"

install:
	@python3 -m venv .venv

test:
	@clear
	@pytest
