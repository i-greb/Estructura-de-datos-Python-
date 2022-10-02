"""Hacer una bicola"""
"""En las bicolas se pueden insertar y extraer datos de ambos lados de la cola"""


class bicolaDinamica:
    __listaCola = []

    def ponerFrente(self, elemento):
        self.__listaCola.insert(0, elemento)

    def ponerFinal(self, elemento):
        self.__listaCola.append(elemento)

    def quitarFrente(self):
        if self.bicolaVacia():
            return False
        else:
            return self.__listaCola.pop(0)

    def quitarFinal(self):
        if self.bicolaVacia():
            return False
        else:
            return self.__listaCola.pop()

    def bicolaVacia(self):
        return len(self.__listaCola) == 0

    def limpiarCola(self):
        self.__listaCola.clear()

    def frente(self):
        if self.bicolaVacia():
            return False
        else:
            return self.__listaCola[0]

    def final(self):
        if self.bicolaVacia():
            return False
        else:
            f = len(self.__listaCola) - 1
            return self.__listaCola[f]

    def mostrarTamBicola(self):
        return len(self.__listaCola)


"""if __name__ == '__main__':
    bicola = bicolaDinamica()

    bicola.ponerFrente(23)
    bicola.ponerFinal(32)
    bicola.ponerFinal(44)
    print(bicola.final())
    f = bicola.quitarFinal()
    print(f)
    print(bicola.final())"""


class bicolaEstatica:
    __tamBicola = int(0)
    __listaCola = []

    def __init__(self, tamBicola):
        self.__tamBicola = tamBicola

    def bicolaVacia(self):
        return len(self.__listaCola) == 0

    def bicolaLLena(self):
        return self.__tamBicola == len(self.__listaCola)

    def PonerFrente(self, elemento):
        if self.bicolaLLena():
            return False
        else:
            self.__listaCola.insert(0, elemento)
            return True

    def PonerFinal(self, elemento):
        if self.bicolaLLena():
            return False
        else:
            self.__listaCola.append(elemento)
            return True

    def QuitarFrente(self):
        if self.bicolaVacia():
            return False
        else:
            return self.__listaCola.pop(0)

    def QuitarFinal(self):
        if self.bicolaVacia():
            return False
        else:
            return self.__listaCola.pop()

    def Frente(self, elemento):
        if self.bicolaLLena():
            return False
        else:
            f = len(self.__listaCola) - 1
            return self.__listaCola[f]

    def Final(self, elemento):
        if self.bicolaLLena():
            return False
        else:
            self.__listaCola.append(elemento)

    def mostrarTamBicola(self):
        return len(self.__listaCola)


if __name__ == '__main__':
    bicola = bicolaDinamica()
    print("Bicolas dinámicas")
    bicola.ponerFrente(23)
    bicola.ponerFinal(32)
    bicola.ponerFinal(44)
    print(bicola.final())
    f = bicola.quitarFinal()
    print(f)
    print(bicola.final())

