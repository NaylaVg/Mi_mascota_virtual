# importar el modulo random
# import imagen desde el archivo mascota.py
import random
from mascota import imagen


class mascotaVirtual:
    def __init__(self, nombre):
        pass

    def alimentar(self):
        pass

    def jugar(self):
        pass

    def estado_animo(self):
        pass

    def presentacion(self):  # opcional
        pass

    def despedida(self):  # opcional
        pass

# Crear una instancia de MascotaVirtual

nombre = input("¿Cómo se llama tu mascota? ")
mi_mascota = mascotaVirtual(nombre)
mi_mascota.presentacion()

# Menú interactivo

while True:
    print("\n--- Menú ---")
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Bañar")
    print("4. Estado de animo")
    print("5. Salir")

    

    try:
        opcion = int(input(f"¿Qué quieres hacer con {nombre}? "))
    except ValueError:
        print("Ingresá un numerito de las opciones flaco no es muy dificil")
        continue  # vuelve al inicio del bucle si hubo error

    match opcion:
        case 1:
            mi_mascota.alimentar()
        case 2:
            mi_mascota.jugar()
        case 3:
            mi_mascota.bañar()
        case 4:
            mi_mascota.estado_animo()
        case 5: 
            mi_mascota.despedida()
            break
        case _:
            print("Ah no pero no seras cornudo vos no? un numerito de las opciones te estoy pidiendo")






# Interactuar con la mascota virtual
# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Si te animas crea una interfaz para poder interactuar con tu mascota
