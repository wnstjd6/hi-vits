from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, services
from .database import get_db

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post_in: schemas.PostCreate, db: Session = Depends(get_db)):
    return services.create_post_service(db, post_in)


@router.get("/{post_id}", response_model=schemas.PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = services.get_post_service(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.get("/", response_model=list[schemas.PostOut])
def list_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_posts_service(db, skip, limit)


@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, post_in: schemas.PostUpdate, db: Session = Depends(get_db)):
    db_post = services.get_post_service(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return services.update_post_service(db, db_post, post_in)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = services.get_post_service(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    services.delete_post_service(db, db_post)
    return None

