from Hotel import Hotel 
from HabitacionEstandar import HabitacionEstandar
from HabitacionSuite import HabitacionSuite
from HabitacionPremium import HabitacionPremium

def menu():
    hotel = Hotel()
    while True:
        print("\n===== SISTEMA DE RESERVAS DE HOTEL =====")
        print("1. Reservar habitación")
        print("2. Cancelar reserva")
        print("3. Mostrar reservas")
        print("4. Salir")
        
        while True:
            opcion = input("Elige una opción (1-4): ")
            if opcion.isdigit():  
                opcion = int(opcion)  
                if 1 <= opcion <= 4:
                    print("Opción válida:", opcion) 
                    break  
                else:
                    print("El número debe estar entre 1 y 4.")
            else:
                print("Debes ingresar un número válido.")
                
        if opcion == 1:
            print("\n==========")
            print("Reservar habitación")
            cliente = input("Nombre del cliente: ")
            documento = input("Documento del cliente: ")
            while True:
                noches = input("Número de noches: ")
                if noches.isdigit():
                    noches = int(noches)
                    if noches > 0:
                        break
                    else:
                        print("El número de noches debe ser mayor a cero.")
                else:
                    print("Debes ingresar un número válido.")
            while True:
                print("Tipos de habitación:")
                print("1. Estándar ($200000/noche)")
                print("2. Suite ($300000/noche)")
                print("3. Premium ($450000/noche)")
                tipo = input("Seleccione tipo: ")

                if tipo.isdigit():
                    tipo = int(tipo)
                    if 1 <= tipo <= 3:
                        print("Opción válida:", tipo)
                        break
                    else:
                        print("El número debe estar entre 1 y 3.")
                else:
                    print("Debes ingresar un número válido.")
            if tipo == 1:
                hotel.reservar(cliente, documento, noches, HabitacionEstandar)
            elif tipo == 2:
                hotel.reservar(cliente, documento, noches, HabitacionSuite)
            elif tipo == 3:
                hotel.reservar(cliente, documento, noches, HabitacionPremium)
            else:
                print("Tipo inválido.")
        elif opcion == 2:
            documento = input("Ingrese el documento del cliente para cancelar la reserva: ")
            hotel.cancelar_reserva(documento)
        elif opcion == 3:
            hotel.mostrar_reservas()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
if __name__ == "__main__":
    menu()