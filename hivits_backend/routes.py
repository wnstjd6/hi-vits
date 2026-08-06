from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from . import schemas, services
from .database import get_db

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post_in: schemas.PostCreate, db: Session = Depends(get_db)):
    return services.create_post_service(db, post_in)

