from abc import ABC, abstractmethod
from ..models.cards import CardFilter

class CardsSource(ABC):
    """ 
    Abstract class that gets Card Data from different Data sources
    like a JSON file, SQL Databases, NoSQL Databases, Flat file, etc.
    """
    
    @abstractmethod
    async def get_cards(self):
        """ Implements getting all cards """