from src.Habitacion import Habitacion

class HabitacionEstandar(Habitacion):
    def __init__(self, numero):
        super().__init__(numero, "Estándar", 200000)
