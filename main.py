from random import randint
from models import Spaceship, Weapon
from uuid import uuid4
from exceptions import FreeSlotError

weapons = []

test = Spaceship('test', randint(300, 1000), randint(0, 5), 3, 3, 3)
for _ in range(10):
    weapons.append(Weapon(uuid4(), randint(30, 100), randint(5, 40), randint(1, 70)))

for weapon in weapons:
    try:
        test.installation_of_weapons(weapon)
    except FreeSlotError as e:
        print(e)
        break
