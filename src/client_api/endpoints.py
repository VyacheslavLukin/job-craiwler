from fastapi import APIRouter
from src.client_api.models import CVModel

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {"msg": "Hello World"}


@router.post("/upload_text_cv")
async def upload_text_cv(cv: CVModel) -> dict[str, str]:
    return {"msg": "CV has been uploaded"}
