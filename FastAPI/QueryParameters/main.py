import imp
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/blog")
def index(limit = 10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {"data": f'{limit} blogs from the db'}
    else:
        return {"data": f'{limit} from the db'}