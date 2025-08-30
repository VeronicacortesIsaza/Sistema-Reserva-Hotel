from src.Habitacion import Habitacion
class HabitacionPremium(Habitacion):
    def __init__(self, numero: int):
        super().__init__(numero, "Premium", 450000)