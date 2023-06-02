from fastapi import FastAPI

app = FastAPI()


@app.get("/upload_text_cv")
async def upload_text_cv():
    return {"message": "CV has been uploaded"}
