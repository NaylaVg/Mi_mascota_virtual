import random

from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 0
        self.hambre = 0
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_feliz = imagen.feliz
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado

    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre == 0: 
            print(self.imagen_disgustado)
            print(self.nombre, "está lleno, no puede comer más!")
        else:
            self.hambre -= random.randint(5, 10)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(self.nombre, "ha sido alimentado!")

  

    def jugar(self):
        pass

    def estado_animo(self):
        pass

    def banarse(self):
        pass

    def dormir(self):
        pass

    def pasear(self):
        pass

    def presentacion(self):
        pass
 
    def despedida(self):
        pass