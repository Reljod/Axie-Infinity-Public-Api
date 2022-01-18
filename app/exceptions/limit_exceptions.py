

class StartLimitException(Exception):
    
    def __init__(self, start_limit) -> None:
        super().__init__(f"Start limit {start_limit} is invalid.\
            Start limit should not be less than 0.")
        
class LimitInvalidException(Exception):
    def __init__(self, limit) -> None:
        super().__init__(f"Limit {limit} is invalid.\
            Limit should not be less than 0.")