from typing import List
from pydantic import BaseModel
from enum import Enum, auto
from typing import List, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod


class CardAttackType(str, Enum):
    MELEE = "melee"
    RANGE = "ranged"
    
class AxieType(str, Enum):
    AQUA = "aqua"
    BEAST = "beast"
    BIRD = "bird" 
    BUG = "bug"
    DAWN = "dawn"
    DUSK = "dusk"
    MECH = "mech"
    REPTILE = "reptile"

class Card(BaseModel):
    part_name: str
    card_name: str
    card_class: AxieType
    attack: int
    shield: int
    attack_type: CardAttackType | None = None
    card_effect: str | None = None
    
class CardList(BaseModel):
    cards: List[Card] = []
    
class CardFilter(ABC):
    
    @abstractmethod
    def filter(self, cards: CardList) -> CardList:
        """ Implementation to filter a list of cards. """

class CardFilterBasic(CardFilter, BaseModel):
    part_name: str | None = None
    card_name: str | None = None
    card_class: AxieType | None = None
    attack_type: CardAttackType | None = None
    
    def filter(self, cards: CardList) -> CardList:
        cards.cards = [card for card in cards.cards if self.is_card_included(card)]
        return cards
    
    def is_card_included(self, card: Card) -> bool:
        
        is_included : bool = self.is_filter_and_card_equal(
            (self.part_name, self.card_name, self.card_class, self.attack_type),
            (card.part_name, card.card_name, card.card_class, card.attack_type)
        )
        
        return is_included
                
    def is_filter_and_card_equal(self, 
                                 filter_parts: Tuple, 
                                 card_parts: Tuple
                                ) -> bool:
        
        is_included : bool = False
        
        for filter_part, card_part in zip(filter_parts, card_parts):
            if filter_part is None:
                continue
            
            is_included = filter_part == card_part
        
        return is_included