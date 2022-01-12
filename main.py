from fastapi import FastAPI, responses, status
from fastapi.openapi.utils import get_openapi
from typing import Dict
from api.ds.datasource_json import CardsSourceFromJSON
from api.models.cards import CardList, CardFilterBasic
from api.models.limit import PaginationLimiter
from api.endpoints import cards_controller as cc 

app = FastAPI()

def custom_openapi() -> Dict[str, any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Axie Infinity Public API",
        version="0.1.0",
        description="Open Source public API containing Axie Infinity Related Data.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": r"https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/")
async def root():
    return responses.RedirectResponse(
        '/docs', 
        status_code=status.HTTP_302_FOUND
    )

@app.post("/cards", response_model=CardList)
async def get_cards(
        filter: CardFilterBasic | None = None, 
        limiter: PaginationLimiter | None = None):
    source = CardsSourceFromJSON()
    cards = await cc.get_cards_controller(
        source, filter, limiter
    )
    return cards