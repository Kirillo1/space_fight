from random import randint
from models import Weapon

test = Weapon('test', randint(30, 100), randint(5, 40), randint(1, 70))
print(test.display())
print(test.action())
print(test.display())

