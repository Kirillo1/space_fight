class TotalVolumeError(ValueError):
    def __init__(self, spaciousness, equipment_taken_capacity, *args: object) -> None:
        super().__init__(*args)
        self.spaciousness = spaciousness
        self.equipment_taken_capacity = equipment_taken_capacity

    def __str__(self) -> str:
        return f"Вместительность корабля {self.spaciousness}, оборудование с весом {self.equipment_taken_capacity} не помещается"
