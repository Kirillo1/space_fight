class EquipmentWornOutError(Exception):
    def __init__(self, equipment_name, *args: object) -> None:
        super().__init__(*args)
        self.equipment_name = equipment_name

    def __str__(self) -> str:
        return f"Оборудование {self.equipment_name} изношено"


