from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles

from app.apis.v1 import v1_routers
from app.db.databases import initialize_tortoise

app = FastAPI(
    default_response_class=ORJSONResponse, docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json"
)

# Mount static files for Silver Mode UI
app.mount("/static", StaticFiles(directory="app/static"), name="static")

initialize_tortoise(app)

app.include_router(v1_routers)
