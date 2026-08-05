from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .database import engine, Base
from . import models  # ensure models are imported so they are registered with Base
from .routes import router as posts_router

app = FastAPI(title="HiVITS Backend")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"detail": exc.errors()})


@app.on_event("startup")
def on_startup():
    # create tables if not present
    Base.metadata.create_all(bind=engine)


app.include_router(posts_router)
