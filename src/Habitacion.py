class Habitacion:
    def __init__(self, numero: int, tipo: str, precio: float):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.__disponible = True
    
    def esta_disponible(self) -> bool:
        return self.__disponible

    def ocupar(self) -> None:
        if not self.__disponible:
            print(f"La habitación {self.numero} no está disponible.")
        self.__disponible = False

    def liberar(self) -> None:
        if self.__disponible:
            print(f"La habitación {self.numero} ya está disponible.")
        self.__disponible = True

    def calcular_costo(self, dias: int) -> float:
        if dias <= 0:
            print("El número de días debe ser mayor que cero.")
            return 0
        return dias * self.precio

    def __str__(self) -> str:
        estado = "disponible" if self.esta_disponible() else "no disponible"
        return f"Hab. {self.numero} ({self.tipo}): ${self.precio} - {estado}"
