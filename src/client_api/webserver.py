from src.client_api import app

def run_server():
    import uvicorn
    uvicorn.run("src.client_api:app", host="0.0.0.0", port=7272, reload=True)


if __name__ == "__main__":
    run_server()


