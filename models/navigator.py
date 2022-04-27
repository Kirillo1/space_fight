from random import randint

from constants import HUNDRED, PERCENT_MAGNETIC_STORM
from models import Equipment


class Navigator(Equipment):
    def __init__(self, name, taken_capacity, accuracy) -> None:
        super().__init__(name, taken_capacity)
        self.accuracy = accuracy

    def action(self):
        accuracy = self.recalculate_of_power(self.accuracy)
        if randint(1, HUNDRED) <= PERCENT_MAGNETIC_STORM:
            accuracy /= 2
            print("Произошла магнитная буря")
        super().action()
        return accuracy

    def display(self):
         parent_display = super().display()
         return f"{parent_display}\n{'Точность':<40}{self.accuracy}"
