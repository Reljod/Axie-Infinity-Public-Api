from typing import List
from pydantic import BaseModel
from enum import Enum, auto
from typing import List
from dataclasses import dataclass


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

class CardFilter(BaseModel):
    part_name: str | None = None
    card_name: str | None = None
    card_class: AxieType | None = None
    attack_type: CardAttackType | None = None
    
    def filter(self, card: Card) -> bool:
        return  self.filter_name(card) and\
                self.filter_by_card_class(card) and\
                self.filter_by_attack_type(card)
    
    def filter_name(self, card: Card) -> bool:
        return  self.part_name == card.part_name or\
                self.card_name == card.card_name or\
                ( self.part_name is None and\
                  self.card_name is None )

    def filter_by_card_class(self, card: Card) -> bool:
        return  self.card_class == card.card_class or\
                self.card_class is None
    
    def filter_by_attack_type(self, card: Card) -> bool:
        return  self.attack_type == card.attack_type or\
                self.attack_type is None