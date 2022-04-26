from random import randint
from models import Armor

test = Armor('test', randint(30, 100), randint(5, 40))
print(test.display())
print(test.action())
print(test.display())

