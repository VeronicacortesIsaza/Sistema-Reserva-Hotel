from src.Habitacion import Habitacion
class Reserva:
    """Una reserva contiene una habitación y un cliente."""

    def __init__(self, habitacion: Habitacion, cliente: str, documento: str, noches: int):
        self.habitacion = habitacion
        self.cliente = cliente
        self.documento = documento
        self.noches = noches
        self.habitacion.ocupar()

    def get_costo_total(self) -> float:
        return self.habitacion.calcular_costo(self.noches)

    def cancelar(self):
        self.habitacion.liberar()

    def __str__(self)-> str:
        return (f"Reserva de {self.cliente} con documento {self.documento} en {self.habitacion} " 
                f"por {self.noches} noches. "
                f"Costo total: ${self.get_costo_total()}")
