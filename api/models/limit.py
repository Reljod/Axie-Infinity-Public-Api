from abc import ABC, abstractmethod
from pydantic import BaseModel, validator
from ..exceptions.limit_exceptions import StartLimitException, LimitInvalidException


class Limiter(ABC):

    @abstractmethod
    def set_limit(self, objList: list) -> list:
        """ Implement setting a limit to a particular list """
        
class PaginationLimiter(Limiter, BaseModel):
    start: int | None = 0
    limit: int | None = -1
    
    @validator('start')
    def start_must_be_positive_integer(cls, v):
        if v < 0:
            raise StartLimitException(v)
        return v
    
    @validator('limit')
    def limit_must_be_valid(cls, v):
        if v < -1 and v is not None:
            raise LimitInvalidException(v)
        return v
    
    def set_limit(self, obj_list: list) -> list:
        if self.limit is None or self.limit == -1:
            return obj_list[ self.start: ]
        
        obj_list_len = len(obj_list)
        if self.limit > obj_list_len:
            self.limit = obj_list_len
        
        return obj_list[ self.start : self.limit ]