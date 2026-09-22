from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Research & Decision Assistant",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "project": "Enterprise Research & Decision Assistant",
        "status": "Phase 1 - project skeleton",
    }
from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Research & Decision Assistant",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "project": "Enterprise Research & Decision Assistant",
        "status": "Phase 1 - project skeleton",
    }
