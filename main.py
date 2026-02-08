from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    ativos = db.query(models.Ativo).all()
    return templates.TemplateResponse("index.html", {"request": request, "ativos": ativos})

@app.post("/add")
def add_ativo(nome: str = Form(...), categoria: str = Form(...), db: Session = Depends(get_db)):
    novo_ativo = models.Ativo(nome=nome, categoria=categoria)
    db.add(novo_ativo)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
@app.get("/delete/{ativo_id}")
def delete_ativo(ativo_id: int, db: Session = Depends(get_db)):
    ativo = db.query(models.Ativo).filter(models.Ativo.id == ativo_id).first()
    if ativo:
        db.delete(ativo)
        db.commit()
    return RedirectResponse(url="/", status_code=303)