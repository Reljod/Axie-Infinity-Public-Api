from api.models import cards, limit
from api.ds import datasource as ds

async def get_cards_controller(
        source: ds.CardsSource, 
        card_filter: cards.CardFilter | None, 
        limiter: limit.Limiter | None):
    
    cards = await source.get_cards()
    
    if card_filter is not None:
        cards = card_filter.filter(cards)
        
    if limiter is not None:
        cards_list = cards.cards
        cards_list = limiter.set_limit(cards_list)
        cards.cards = cards_list
        
    return cards