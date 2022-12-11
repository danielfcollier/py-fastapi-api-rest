create:
	@python3 -m venv .venv

install:
	@pip install -r requirements.txt

run:
	@uvicorn src.main:app --reload --host 0.0.0.0 --port 4000

venv:
	@echo "run with: source .venv/bin/activate"
	@echo "stop with: deactivate"

tunnel:
	@ngrok http 4000

test:
	@clear
	@pytest
