from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="views")


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