from abc import ABC, abstractmethod
class Eletronico(ABC):
    preco_base = 1000
    Eletronicos_cadastrados = 0
    def __init__(self, marca): 
        self.marca = marca
        Eletronico.Eletronicos_cadastrados += 1

    def get_marca(self):
        return self.marca
    def set_marca(self, novo_marca):
        self.marca = novo_marca    
    

    @abstractmethod
    def preco(self):
        pass

    @classmethod
    def get_preco_base(self):
        return self.preco_base
    @classmethod
    def set_preco_base(self, novo_preco_base):
        self.preco_base = novo_preco_base
    def get_quantidade_Eletronicos(self):
        return self.get_quantidade_Eletronicos
    def set_quantidade_Eletronicos(self, nova_quantidade):
        self.Eletronicos_cadastrados = nova_quantidade
    def __str__(self):
        return f'Eletronicos cadastrados:{self.Eletronicos_cadastrados}.'
    def quantidade_objetos(self, Cadastros):
        self.Eletronicos_cadastrados = Cadastros
        return Cadastros
    

class Televisao(Eletronico):
    def __init__(self, marca):
        super().__init__(marca)
    def preco(self):
        return self.preco_base * 1.5
    def __str__(self):
        s = f'Marca Televisão:{self.marca}.'
        return s
    
class Celular(Eletronico):
    def __init__(self, marca):
        super().__init__(marca)
    def preco(self):
        return self.preco_base * 3.2
    def __str__(self):
        s = f'Marca Celular:{self.marca}.'
        return s
        

if __name__ == '__main__':
    Televisao1 = Televisao('Apple')
    Celular1 = Celular('Samsung')


    print(Televisao1)
    print(f'Preço Televisao: {Televisao1.preco():.2f} ')
    print(Celular1)
    print(f'Preço Celular: {Celular1.preco():.2f}')
    print('Quantidade de Eletronicos Cadastrados:', Televisao1.get_quantidade_Eletronicos())
    


    
