from constants import MAX_WEAR_CONDITION, WEAR_STEP
from exceptions import EquipmentWornOutError


class Equipment:
    def __init__(self, name, taken_capacity) -> None:
        self.wear_condition = 0
        self.name = name
        self.taken_capacity = taken_capacity

    def action(self):
        if self.wear_condition > MAX_WEAR_CONDITION:
            self.wear_condition = MAX_WEAR_CONDITION
        self.check_for_complete_wear()
        self.wear_condition += WEAR_STEP

    def check_for_complete_wear(self):
        if self.wear_condition == MAX_WEAR_CONDITION:
            raise EquipmentWornOutError(self.name)

    def recalculate_of_power(self, value):
        return value - value * self.wear_condition / 100

    def display(self):
        return f"{'Название оборудования':<40}{self.name}\n{'Уровень износа':<40}{self.wear_condition}\n{'Объём':>40}{self.taken_capacity}"
