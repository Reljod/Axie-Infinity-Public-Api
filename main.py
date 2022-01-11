from fastapi import FastAPI, responses, status

from api.ds.datasource_json import CardsSourceFromJSON
from api.models.cards import CardList, CardFilterBasic
from api.models.limit import PaginationLimiter
from api.endpoints import cards_controller as cc

app = FastAPI()

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