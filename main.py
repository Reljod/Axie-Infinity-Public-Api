from fastapi import FastAPI, responses, status

from api.ds.datasource_json import JsonDataSource
from api.models.cards import CardList, CardFilter

app = FastAPI()

@app.get("/")
async def root():
    return responses.RedirectResponse(
        '/docs', 
        status_code=status.HTTP_302_FOUND
    )

@app.post("/cards", response_model=CardList)
async def get_cards(filter: CardFilter | None = None):
    jds = JsonDataSource()
    cards = await jds.get_cards(filter)
    return cards