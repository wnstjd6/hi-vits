from sqlalchemy.orm import Session
from . import models, schemas


def create_post(db: Session, post_in: schemas.PostCreate) -> models.Post:
    db_post = models.Post(title=post_in.title, content=post_in.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def update_post(db: Session, db_post: models.Post, post_in: schemas.PostUpdate):
    if post_in.title is not None:
        db_post.title = post_in.title
    if post_in.content is not None:
        db_post.content = post_in.content
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, db_post: models.Post):
    db.delete(db_post)
    db.commit()

