from typing import List
from pydantic import BaseModel
from enum import Enum, auto
from typing import List
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
        return  self.is_name_equals_or_none(card) and\
                self.is_card_class_equals_or_none(card) and\
                self.is_attack_type_equals_or_none(card)
    
    def is_name_equals_or_none(self, card: Card) -> bool:
        return  self.part_name == card.part_name or\
                self.card_name == card.card_name or\
                ( self.part_name is None and\
                  self.card_name is None )

    def is_card_class_equals_or_none(self, card: Card) -> bool:
        return  self.card_class == card.card_class or\
                self.card_class is None
    
    def is_attack_type_equals_or_none(self, card: Card) -> bool:
        return  self.attack_type == card.attack_type or\
                self.attack_type is None