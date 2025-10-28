import random

# importar el modulo random
# import imagen desde el archivo mascota.py
import random
from mascota import imagen
import random
from mascota import imagen


class mascotaVirtual:
    def __init__(self, nombre):
        self.felicidad = 0
        self.hambre = 0
        self.suciedad = 0
        self.sueño = 0
        self.nombre = nombre
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_feliz = imagen.feliz
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado



    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if  self.felicidad < 0:
            self.felicidad = 0
        if  self.hambre == 0: 
            print(self.imagen_disgustado)
            print(self.nombre, "está lleno, no puede comer más!")
        else:
            self.hambre -= random.randint(5, 10)
            if  self.hambre < 0:
                self.hambre = 0
                print(self.imagen_feliz)
                print(self.nombre, "ha sido alimentado!")

  

    def jugar(self):
        if self.hambre <= 70:
            print(imagen.feliz)
            print(self.nombre, "se divierte")
            self.felicidad += random.randint(5, 10)
        if self.felicidad >= 100:
            self.felicidad = 100
            self.hambre += random.randint(5, 10)
        if self.hambre >= 100:
             self.hambre = 100
        else: 
          print(self.nombre, "tiene mucha hambre y no puede jugar")
        

    def banarmascota(self):
        self.suciedad -= (100)
        if  self.suciedad <= 0:
            self.suciedad = 0
            print(imagen.feliz)
            print('Su mascota esta limpiecita y FELIZ! :>')

        if  self.suciedad >= 10:
            print(imagen.triste)
            print('oh no, tu mascota esta chuchia :c')
          
    def estado_animo(self):
        print(f'\n{nombre} tiene:\n{self.felicidad} puntos de felicidad')
        print(f'{self.hambre} puntos de hambre')
        print(f'{self.suciedad} puntos de mugre')
        print(f'{self.sueño} puntos de noni')
        pass

    def dormir(self):
        self.sueño -= 100
        if  self.sueño <= 0:
            self.sueño = 0
            self.felicidad += random.randint(10,15)
            print(imagen.feliz)
            print(nombre, 'Ya descanso plasidamente')


    def pasear(self):
        pass

    def presentacion(self):
        pass
 
    def despedida(self):
        print("Un gusto haber jugado contigo ˇvˇ, nos vemos para la proxima")
    
    def muerteinstantanea(self):
        print(imagen.muerto)
        print('¿¿¡¡ QUE HAS HECHO!!??, LO ACARICIASTE DEMASIADO FUERTE,  ¡¡Y MATASTEE A', nombre, 'Ọ⌂Ọ !!')

# Crear una instancia de MascotaVirtual

nombre = input("¿Cómo se llama tu mascota?: ")
mi_mascota = mascotaVirtual(nombre)
mi_mascota.presentacion()

# Menú interactivo

while True:
    print("\n--- Menú ---")
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Dormir")
    print("4. Bañar")
    print("5. Estado de animo")
    print("6. Salir")
    print("7. ♥Acariciar fuerte♥")
    

    try:
        opcion = int(input(f"¿Qué quieres hacer con {nombre}? "))
    except  ValueError:
            print("Ingresá un numerito de las opciones flaco no es muy dificil")
            break  # vuelve al inicio del bucle si hubo error

    match opcion:
        case 1:
            mi_mascota.alimentar()
        case 2:
            mi_mascota.jugar()
        case 3:
            mi_mascota.dormir()
        case 4:
            mi_mascota.banarmascota()
        case 5:
            mi_mascota.estado_animo()
        case 6: 
            mi_mascota.despedida()
            break
        case 7:
            mi_mascota.muerteinstantanea()
            break
        case _:
            print("Ah no pero no seras cornudo vos no? un numerito de las opciones te estoy pidiendo")
