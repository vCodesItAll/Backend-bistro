from sqlalchemy.orm import Session
from models import MenuItem



def get_menu_items(db: Session):
    return db.query(MenuItem).all()

