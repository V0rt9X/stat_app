from fastapi import FastAPI

app = FastAPI(title="stat_app")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
