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
        pass



    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if  self.hambre > 100:
            self.hambre = 100
        if  self.felicidad < 0:
            self.felicidad = 0
            self.hambre <= 0
            print(f'{imagen.disgustado}')
            print(f'{nombre}, está lleno, no puede comer más!')
        else:
            print(f'{imagen.feliz}')
            print(f'{nombre}, "ha sido alimentado!"')
            pass

    def jugar(self):
        while True:
            print("\n")
            print(f"¿A que te gustaría jugar con {nombre}?")
            print("1. lanzar pelota")
            print("2. Correr por el parque")
            print("3. Saltar obstáculos")
            print("4. Dejar de jugar")


            try:
                opcion = int(input(f"¿Qué quieres jugar con {nombre}? "))
            except  ValueError:
                print("No loco, no sabes que es un numero?")
                break
                
            match opcion:

                case 1:
                    print(f"\n {nombre} Tu mascota corre feliz a buscar la pelota")
                    if  self.felicidad > 100:
                        self.felicidad = 100
                    self.felicidad += random.randint(10,15)
                    if   self.suciedad > 100:
                        self.suciedad = 100
                    self.suciedad += random.randint(5,10)
                    if    self.hambre > 100:
                        self.hambre = 100
                    self.hambre +=random.randint(10,15)
                    if    self.sueño > 100:
                        self.sueño = 100
                    self.sueño += random.randint(10,15)

                case 2:
                    print(f"\n {nombre} corre a toda velocidad por el parque ")
                    if  self.felicidad > 100:
                        self.felicidad = 100
                    self.felicidad += random.randint(10,15)
                    if  self.suciedad > 100:
                        self.suciedad = 100
                    self.hambre += random.randint(10,15)
                    if  self.hambre > 100:
                        self.hambre = 100
                    self.suciedad += random.randint(10,15)
                    if  self.sueño > 100:
                        self.sueño = 100
                    self.sueño += random.randint(10,15)
                     
                case 3:
                    print(f"\n {nombre} salta los obstáculos como un campeón!")
                    if  self.felicidad > 100:
                        self.felicidad = 100
                    self.felicidad += random.randint(10,15)
                    if  self.suciedad > 100:
                        self.suciedad = 100
                    self.hambre += random.randint(10,15)
                    if  self.hambre > 100:
                        self.hambre = 100
                    self.suciedad += random.randint(10,15)
                    if  self.sueño > 100:
                        self.sueño = 100
                    self.sueño += random.randint(10,15)
                    
                case 4:
                    print(f'{imagen.feliz}')
                    print(f"\n a {nombre} le gusto mucho jugar, se lo ve agradecirdo")
                    break
                case _:
                    print("\n Esa opción no existe ")
                    pass


    def banarmascota(self):
        self.suciedad -= random.randint(5, 10)
        if  self.suciedad < 0:
            self.suciedad = 0
            print(imagen.feliz)
            print('Su mascota esta limpiecita y FELIZ! :>')
            pass

          
    def estado_animo(self):
        print(f'\n{nombre} tiene:\n{self.felicidad} puntos de felicidad')
        print(f'{self.hambre} puntos de hambre')
        print(f'{self.suciedad} puntos de mugre')
        print(f'{self.sueño} puntos de noni')
        pass

    def dormir(self):
        self.sueño -= random.randint(5,10)
        if  self.sueño < 0:
            self.sueño = 0
            self.felicidad += random.randint(10,15)
            self.sueño == 0
            print(f'{imagen.enojado}')
            print(f'{nombre} ya no quiere dormir mas')
        
        else: 
            print(f'{imagen.dormido}')
            print(nombre, 'Ya descanso plasidamente')
            pass


    def pasear(self):
        pass

    def presentacion(self):
        print (f'¡HOLA!, yo soy {nombre} y voy a ser tu mascota. !DIVIRMANOS¡')
        pass
 
    def despedida(self): 
        print(imagen.triste)
        print("no puedo creer que me estes por dejar, te hechare de menos. \n")
        pass
    
    def muerteinstantanea(self):
        print(imagen.muerto)
        print('¿¿¡¡ QUE HAS HECHO!!??, LO ACARICIASTE DEMASIADO FUERTE,  ¡¡Y MATASTEE A', nombre, 'Ọ⌂Ọ !!')
        pass

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
