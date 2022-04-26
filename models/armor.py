from models import Equipment


class Armor(Equipment):
    def __init__(self, name, taken_capacity, defence) -> None:
        super().__init__(name, taken_capacity)
        self.defence = defence

    def action(self):
        defence = self.recalculate_of_power(self.defence)
        super().action()
        return defence

    def display(self):
         parent_display = super().display()
         return f"{parent_display}\n{'Защита':<40}{self.defence}"
