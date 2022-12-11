# REST API App

Requirements: Python 3.10 + FastAPI

## Table of Contents

- [Demo Version](#demo-version)
- [Build and Run](#build-and-run)
- [Run Tests](#run-tests)
- [CI-CD](#ci-cd)
- [References](#references)

## Demo Version

Run locally with `ngrok`:

```bash
make tunnel
```

## Build and Run the App

### Locally:

1) Create the virtual environment:

```bash
python3 -m venv .venv
```

2) Activate the virtual environment:

```bash
source .venv/bin/activate
```

3) Install the required modules:

```bash
pip install -r requirements.txt
```

4) Run the server? 

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 4000
```

### With Docker:

```bash
docker build -t api-rest .
docker run -m 512m --memory-reservation=256m -p 4000:4000 api-rest
```

## Run Tests

```bash
pytest
```

## CI-CD

### GitHub Actions

Tests are configured to run on multiple OS and Node.js versions to make sure the app is compatible across many platforms.

#### Test locally with `act`

```bash
act -j tests
```

### Deployment to Production Branch

If tests are passing, the CI with GitHub Actions pushes the changes to a production branch (`prod`).

## Configurations

### Add a New Controller with:

```bash
npx nest g controller <route>
```

## References

### FastAPI documentation:

https://fastapi.tiangolo.com/

### Ngrok

https://ngrok.com

### Test GitHub Actions Locally

https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-net

https://github.com/nektos/act
