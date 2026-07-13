from fastapi import FastAPI

app = FastAPI(
    title="Foodery API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Hello, Foodery!"
    }