from src.HabitacionEstandar import HabitacionEstandar
from src.HabitacionSuite import HabitacionSuite
from src.HabitacionPremium import HabitacionPremium
from src.Reserva import Reserva

class Hotel:
    """Clase que administra habitaciones y reservas."""

    def __init__(self):
        self.habitaciones = []
        for i in range(101, 200):
            self.habitaciones.append(HabitacionEstandar(i))

        for i in range(201, 300):
            self.habitaciones.append(HabitacionSuite(i))

        for i in range(301, 400):
            self.habitaciones.append(HabitacionPremium(i))
        self.reservas = []

    def reservar(self, cliente: str, documento: str, noches: int, tipo_habitacion) -> Reserva | None:
        for habitacion in self.habitaciones:
            if isinstance(habitacion, tipo_habitacion) and habitacion.esta_disponible():
                reserva = Reserva(habitacion, cliente, documento, noches)
                self.reservas.append(reserva)
                print("Reserva realizada con éxito.")
                return reserva
        print("No hay habitaciones disponibles de ese tipo.")
        return None

    def cancelar_reserva(self, documento: str) -> None:
        for reserva in self.reservas:
            if reserva.documento == documento:
                reserva.cancelar()
                self.reservas.remove(reserva)
                print("Reserva cancelada correctamente.")
                return
        print("No se encontró una reserva con ese documento.")

    def mostrar_reservas(self) -> None:
        if not self.reservas:
            print("No hay reservas activas.")
        else:
            for r in self.reservas:
                print(r)