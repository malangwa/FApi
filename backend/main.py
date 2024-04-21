from fastapi import FastAPI
app = FastAPI(title="Jobboard API",version="0.1")

@app.get("/")
def read_root():
    return {"Hello": "World"}
