from sqlalchemy.orm import Session
from . import crud, schemas


def create_post_service(db: Session, post_in: schemas.PostCreate):
    return crud.create_post(db, post_in)

