# Example file for Advanced Python: Language Features by Joe Marini
# define enumerations using the Enum base class
from enum import Enum, auto

# enums have human-readable values and types
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


# enums have name and value properties
print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))

# print the auto-generated value
print(Fruit.PEAR.value)

# enums are hashable - can be used as keys
my_fruits = {}
my_fruits[Fruit.BANANA] = "Come Mr.Tallyman"
print(my_fruits[Fruit.BANANA])
