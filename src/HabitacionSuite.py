from src.Habitacion import Habitacion
class HabitacionSuite(Habitacion):
    def __init__(self, numero: int):
        super().__init__(numero, "Suite", 300000)