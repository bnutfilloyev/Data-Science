from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_read():
    return {"message": "Hello World"}
