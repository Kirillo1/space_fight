class FreeSlotError(Exception):

    def __init__(self, equipment_type, *args: object) -> None:
        super().__init__(*args)
        self.equipment_type = equipment_type

    def __str__(self) -> str:
        return f"Слоты для {self.equipment_type} оборудования закончены"
