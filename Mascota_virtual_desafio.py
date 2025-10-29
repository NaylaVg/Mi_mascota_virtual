# importar el modulo random
# import imagen desde el archivo mascota.py
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
        self.imagen_dormido = imagen.dormido
        self.imagen_enojado = imagen.enojado



    def alimentar(self):

        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
           self.felicidad = 0

        if self.hambre == 0:                                        
            print(f"{self.nombre} está lleno, no puede comer más")
            print(f"{self.imagen_disgustado}")
            return

        self.hambre -= random.randint(10, 15)
        if self.hambre < 0:
            self.hambre = 0

        print(f"{self.imagen_feliz}")
        print(f"{self.nombre} ha sido alimentado!")


    def jugar(self):
        if self.hambre > 70:
            print("Tiene mucha hambre y no puede jugar.")
            return

        while True:
            print("\n¿A qué te gustaría jugar con", self.nombre, "?")
            print("1. Lanzar pelota")
            print("2. Correr por el parque")
            print("3. Saltar obstáculos")
            print("4. Dejar de jugar")
            
            try:                
                opcion = int(input(f"¿Qué quieres jugar con {self.nombre}? "))
            except ValueError:
                print("Ingresá un número válido.")
                break

            if opcion == 4:
                print(self.imagen_feliz)
                print(f"A {self.nombre} le gustó mucho jugar, se lo ve agradecido.")
                break
            elif opcion in (1, 2, 3):
                self.felicidad += random.randint(10, 15)
                if self.felicidad > 100:
                    self.felicidad = 100

                self.hambre += random.randint(10, 15)
                if self.hambre > 100:
                    self.hambre = 100

                self.suciedad += random.randint(5, 10)
                if self.suciedad > 100:
                    self.suciedad = 100

                self.sueño += random.randint(10, 15)
                if self.sueño > 100:
                    self.sueño = 100


                if opcion == 1:
                    print(f"\n{self.nombre} corre feliz a buscar la pelota.")
                elif opcion == 2:
                    print(f"\n{self.nombre} corre a toda velocidad por el parque.")
                else:
                    print(f"\n{self.nombre} salta los obstáculos como un campeón!")
            else:
                print("Esa opción no existe.")


    def banarmascota(self):
        self.suciedad -= random.randint(5, 10)
        if self.suciedad < 0:
            self.suciedad = 0
        print(self.imagen_feliz)
        print(f"{self.nombre} está limpiecito y feliz!")


          
    def estado_animo(self):
        print(f'\n{self.nombre} tiene:')
        print(f'{self.felicidad} puntos de felicidad')
        print(f'{self.hambre} puntos de hambre')
        print(f'{self.suciedad} puntos de mugre')
        print(f'{self.sueño} puntos de sueño')

        if self.hambre >= 70 and self.felicidad <= 50:
            print(self.imagen_triste)
            print("Está muy hambrienta y muy triste.")
        elif self.hambre >= 70:
            print(self.imagen_disgustado)
            print("Está muy hambrienta.")
        elif self.felicidad <= 50:
            print(self.imagen_triste)
            print("Está muy triste.")
        else:
            print(self.imagen_feliz)
            print("Está contenta y satisfecha.")


    def dormir(self):
        self.sueño -= random.randint(5,10)
        if  self.sueño < 0:
            self.sueño = 0

        if self.sueño == 0:
            print(self.imagen_enojado)
            print(f"{self.nombre} ya no quiere dormir más.")
        else:
            self.felicidad += random.randint(10, 15)
            if self.felicidad > 100:
                self.felicidad = 100
            print(self.imagen_dormido)
            print(f"{self.nombre} ya descansó plácidamente.")



    def pasear(self):
        if self.hambre > 70:
            print(f"{self.nombre} tiene demasiada hambre y no quiere salir a pasear.")
            return
        if self.sueño > 70:
            print(f"{self.nombre} está demasiado cansado para pasear.")
            return

        self.felicidad += random.randint(15, 25)
        if self.felicidad > 100:
            self.felicidad = 100

        self.hambre += random.randint(10, 15)
        if self.hambre > 100:
            self.hambre = 100

        self.suciedad += random.randint(5, 10)
        if self.suciedad > 100:
            self.suciedad = 100

        self.sueño += random.randint(10, 15)
        if self.sueño > 100:
            self.sueño = 100

        print(self.imagen_feliz)
        print(f"{self.nombre} salió a pasear y se divirtió mucho.")

    def presentacion(self):
            print (f'¡HOLA!, yo soy {self.nombre} y voy a ser tu mascota. !DIVIRMANOS¡')
        
 
    def despedida(self): 
            print(self.imagen_triste)
            print("no puedo creer que me estes por dejar, te hechare de menos. \n")
        
    
    def muerteinstantanea(self):
        print(self.imagen_muerto)
        print(f'¿¿¡¡ QUE HAS HECHO!!?? LO ACARICIASTE DEMASIADO FUERTE  ¡¡Y MATASTEE A {self.nombre} Ọ⌂Ọ !!')



nombre = input("¿Cómo se llama tu mascota?: ")
mi_mascota = mascotaVirtual(nombre)
mi_mascota.presentacion()



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
            break  
    
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