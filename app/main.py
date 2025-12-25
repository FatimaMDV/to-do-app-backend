from fastapi import FastAPI

app = FastAPI(title="To-Do App Backend")

@app.get("/health")
def health():
    return {"status": "ok"}
