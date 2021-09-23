from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.sql.operators import exists

from wee.database.database import session
from wee.database.models import URL

app = FastAPI()

class NewURL(BaseModel):
    id: Optional[str]
    url: str


@app.get("/{url}")
async def read_item(url):
    url = list(session.query(URL).filter(URL.id==url))
    if len(url) > 0:
        return RedirectResponse(url[0].url)
    
    raise HTTPException(status_code=404, detail="That url does not exist")

@app.get("/{url}/raw")
async def read_item(url):
    url = list(session.query(URL).filter(URL.id==url))
    if len(url) > 0:
        return {"id":url[0].id, "url":url[0].url}
    
    raise HTTPException(status_code=404, detail="That url does not exist")

@app.post("/")
async def make_shortcut(url: NewURL):
    exists = list(session.query(URL).filter(URL.id==url.id))
    if url.id:
        if exists:
            raise HTTPException(status_code=409, detail=f"the url '127.0.0.1:8000/{url.id}' already exists")
        shorten = URL(url=url.url, id=url.id)
    else:
        shorten = URL(url=url.url)
    
    session.add(shorten)  
    session.commit()
    return {"url":f"127.0.0.1:8000/{shorten.id}"}
