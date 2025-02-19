import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()  # create an instance of FastAPI
# Указываем папку для статических файлов
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Указываем папку с шаблонами
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)  # Начало
async def read_root(request: Request):
    # Передаем запрос и имя шаблона в метод render
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/daniel", response_class=HTMLResponse)  # Портфолио Даниила
async def read_Daniel(request: Request):
    return templates.TemplateResponse("Daniel.html", {"request": request})


@app.get("/viktor", response_class=HTMLResponse)
async def read_Viktor(request: Request):
    image_url = "/static/file/img/Viktor.jpg"  # Указываем путь к изображению
    return templates.TemplateResponse("Viktor.html", {"request": request, "image_url": image_url})


@app.get("/viktor/1", response_class=HTMLResponse)
async def read_Viktor_1(request: Request):
    image_url = "/static/file/img/Viktor.jpg"
    return templates.TemplateResponse("Viktor_1.html", {"request": request, "image_url": image_url})
