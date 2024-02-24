from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    qtd_figura = 0
    l_figura = list()
    @classmethod
    def get_figura(cls):
        return cls.qtd_figura
    def __init__(self):
        FormaGeometrica.qtd_figura +=1
        FormaGeometrica.l_figura.append(self)
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def mensagem(self):
        print('Método concreto de superclasse abstrata FormaGeometrica que herda de ABC.')
    def mensagem2(self):
        print('Método concreto de superclasse abstrata FormaGeometrica que herda de ABC.')
        print('Dados do objeto:', self)
    def mensagem3(self):
        print('Método concreto de superclasse abstrata FormaGeometrica que herda de ABC.')
        print('Nome da classe:', self.__class__.__name__)
class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, novo_valor):
        self.lado = novo_valor
    def area(self):
        vl_area = self.lado ** 2
        return vl_area
    def perimetro(self):
        vl_perimetro = 4 * self.lado
        return vl_perimetro

class Circulo(FormaGeometrica):
    def __init__(self, raio=1):
        self.raio = raio
    def get_raio(self):
        return self.raio
    def set_raio(self, novo_raio):
        self.raio = novo_raio
    def area(self):
        vl_area = 3.14 * pow(self.raio, 2)
        return vl_area
    def perimetro(self):
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro
if __name__ == '__main__':
    #obj_forma = FormaGeometrica()
    obj_quad = Quadrado(3)
    print(obj_quad)