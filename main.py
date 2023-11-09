from fastapi import FastAPI, Depends
import fastapi
from models import  MenuItem, Cuisine, Category, Base
from database import SQLALCHEMY_DATABASE_URL, engine, SessionLocal
from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from crud import get_menu_items
# from routers import heroes

app = FastAPI()

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/menu-items")
def read_menu_items(db: Session = Depends(get_db)):
    menu_items = get_menu_items(db)
    return menu_items


