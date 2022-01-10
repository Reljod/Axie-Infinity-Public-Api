from enum import Enum

class AxieClass(str, Enum):
    BEAST = "beast"
    AQUA = 2
    
if __name__ == '__main__':
    print(AxieClass.BEAST)
    class1 = AxieClass.AQUA
    
    print(class1)