import abc
from ..models.cards import CardList

class DataSource(abc.ABC):
    
    @abc.abstractmethod
    def get_cards(self):
        print("Getting Card List from Data Source")
        raise NotImplementedError