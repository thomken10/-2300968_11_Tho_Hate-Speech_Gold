from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

# initialize fast api
app = FastAPI()

@app.get("/")

async def index():
    return JSONResponse(
        content ={
            "ok":True,
            "code": 200,
            "data": {
                "version":"1.0.0"
                },
                "message":"Success"
        }
    )
# import file from /routers
from routers import cleansing
from routers import sentiment

app.include_router(cleansing.router, tags=["Cleansing API"])
app.include_router(sentiment.router, tags=["Sentiment API"])