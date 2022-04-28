from constants import MAX_SPACESHIP_HEALTH, EQUIPMENT_TYPES
from exceptions import TotalVolumeError, FreeSlotError


class Spaceship:
    def __init__(self, name, spaciousness, accuracy, armor_slots_count,
                 weapon_slots_count, navigator_slots_count) -> None:
        self.name = name
        self.spaciousness = spaciousness
        self.accuracy = accuracy
        self.armor_slots_count = armor_slots_count
        self.weapon_slots_count = weapon_slots_count
        self.navigator_slots_count = navigator_slots_count
        self.health = MAX_SPACESHIP_HEALTH
        self.defence = (1 / (spaciousness * weapon_slots_count)) * 10 ** 4
        self.armor_slots = []
        self.weapon_slots = []
        self.navigator_slots = []

    def installation_of_weapons(self, weapon):
        if self.spaciousness - weapon.taken_capacity < 0:
            raise TotalVolumeError(self.spaciousness, weapon.taken_capacity)
        if not self.weapon_slots_count:
            raise FreeSlotError(EQUIPMENT_TYPES[1])
        self.weapon_slots.append(weapon)
        self.weapon_slots_count -= 1
        self.spaciousness -= weapon.taken_capacity

    def installation_of_armors(self, armor):
        if self.spaciousness - armor.taken_capacity < 0:
            raise TotalVolumeError(self.spaciousness, armor.taken_capacity)
        if not self.armor_slots_count:
            raise FreeSlotError(EQUIPMENT_TYPES[0])
        self.armor_slots.append(armor)
        self.armor_slots_count -= 1
        self.spaciousness -= armor.taken_capacity

    def installation_of_navigators(self, navigator):
        if self.spaciousness - navigator.taken_capacity < 0:
            raise TotalVolumeError(self.spaciousness, navigator.taken_capacity)
        if not self.navigator_slots_count:
            raise FreeSlotError(EQUIPMENT_TYPES[2])
        self.navigator_slots.append(navigator)
        self.navigator_slots_count -= 1
        self.spaciousness -= navigator.taken_capacity

