import fastapi
import uvicorn


api = fastapi.FastAPI()


@api.get("/")
def index():
    return "Hello Weather App"


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
