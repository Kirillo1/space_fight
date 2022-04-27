from random import randint
from models import Navigator

test = Navigator('test', randint(30, 100), randint(5, 40))
print(test.display())
print(test.action())
print(test.display())

