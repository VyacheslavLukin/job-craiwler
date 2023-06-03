from pydantic import BaseModel, validator


class CVModel(BaseModel):
    content: str
    author: str | None = None

    @validator("content")
    def check_cv_len(cls, v):
        if len(v) > 1000:
            raise ValueError("CV length exceeds 1000 words")
        return v

    @validator("content")
    def check_cv_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError("Content is missing ")
        return v
