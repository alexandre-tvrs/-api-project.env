import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from core.settings import get_settings
from redoc.redoc import get_redoc_html
from core.database import engine, Base
from src.projects import routers as routers_projects


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    testing=settings.testing,
    docs_url=None,
    redoc_url=None,
)

app.openapi_version = "3.0.0"

Base.metadata.create_all(bind=engine)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def get_redoc() -> HTMLResponse:
    title = app.title
    return get_redoc_html(openapi_url=app.openapi_url, title=title)

app.include_router(routers_projects.router)

if (__name__) == "__main__":
    print("Using environment: " + settings.enviroment)
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )