from fastapi import FastAPI

from app.api.views import regex_service
from app.api.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/regex/openapi.json", docs_url="/api/v1/regex/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(regex_service, prefix='/api/v1/regex', tags=['regex'])
