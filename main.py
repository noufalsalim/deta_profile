import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

TAG = os.getenv("TAG")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/{id}", response_class=HTMLResponse)
def index(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})