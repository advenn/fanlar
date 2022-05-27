import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")

templates = Jinja2Templates(directory="views")
init_path = "static"
full = os.path.join("views", "static")


@app.route("/")
async def index(request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.route("/xia")
async def xia(request):
    return templates.TemplateResponse("xia.html", {"request": request})


@app.route("/pm")
async def pm(request):
    return templates.TemplateResponse("pm.html", {"request": request})


@app.route("/mis")
async def mis(request):
    return templates.TemplateResponse("mis.html", {"request": request})


@app.route("/nur")
async def pics(request):
    pics = os.listdir(full)
    pics = [os.path.join(init_path, pic) for pic in pics]

    return templates.TemplateResponse("nur.html", {"request": request, "pics": pics})
