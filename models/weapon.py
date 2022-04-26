from .equipment import Equipment
from constants import HUNDRED, PERCENT_MAXIMUM_DAMAGE, CRITICAL_DAMAGE_PERCENT
from random import randint


class Weapon(Equipment):
    def __init__(self, name, taken_capacity, min_damage, critical_hit_chance) -> None:
        super().__init__(name, taken_capacity)
        self.min_damage = min_damage
        self.critical_hit_chance = critical_hit_chance
        self.max_damage = self.min_damage + self.min_damage // HUNDRED * PERCENT_MAXIMUM_DAMAGE

    def action(self):
        if randint(1, HUNDRED) <= CRITICAL_DAMAGE_PERCENT:
            return 0
        if randint(1, HUNDRED) <= self.critical_hit_chance:
            damage = self.max_damage + self.max_damage // HUNDRED * PERCENT_MAXIMUM_DAMAGE
        else:
            damage = randint(self.min_damage, self.max_damage)
        damage = self.recalculate_of_power(damage)
        super().action()
        return damage

    def display(self):
        parent_display = super().display()
        return f"{parent_display}\n{'Минимальный урон':<40}{self.min_damage}\n{'Максимальный урон':<40}{self.max_damage}\n{'Вероятность критического урона':<40}{self.critical_hit_chance}"
