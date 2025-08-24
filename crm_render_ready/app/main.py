from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import init_db

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def startup():
    init_db()

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('dashboard.html', {'request': request})

@app.get('/login', response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})

@app.post('/login', response_class=HTMLResponse)
def login_post(request: Request, email: str = Form(...), password: str = Form(...)):
    if email == 'admin@example.com' and password == 'admin':
        return templates.TemplateResponse('dashboard.html', {'request': request})
    return templates.TemplateResponse('login.html', {'request': request, 'error': 'Credenziali errate'})

@app.get('/kanban', response_class=HTMLResponse)
def kanban(request: Request):
    return templates.TemplateResponse('kanban.html', {'request': request})
