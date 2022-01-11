import json

from .datasource import CardsSource
from ..models.cards import CardList, Card, CardFilter

class CardsSourceFromJSON(CardsSource):
    
    CARDS_LIST = "./api/ds/initialcarddata.json"
    
    async def get_cards(self):
        
        cards = await self._read_json_file()
        self.all_cards = cards.get("cards")
        
        card_list = CardList()
        
        if self.all_cards is None:
            return card_list
        
        for card in self.all_cards:
            card_obj = Card(
                part_name=card.get("part-name"),
                card_name=card.get("card-name"),
                card_class=card.get("card-class"),
                attack=card.get("attack"),
                shield=card.get("shield"),
                attack_type=card.get("attack-type"),
                card_effect=card.get("card-effect")
            )
            
            card_list.cards.append(card_obj)
        
        return card_list
    
    async def _read_json_file(self):
        
        cards_list_dict = {}
        with open(self.CARDS_LIST, "r") as rb:
            cards_list = rb.read()
            cards_list_dict = json.loads(cards_list)
            
        return cards_list_dict