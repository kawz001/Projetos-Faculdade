"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- Analise o problema de locação de Eletronicos e o valor da diária.

- O valor do preço básico de locação é o mesmo (R$ 100.00) para os dois tipos de Eletrônico,
como podemos melhorar as classes retirando código redundante.

Obs.: RN (Regra de Negócio) para o Eletrônico econômico:
      O preço da diária corresponde ao preço base de locação acrescido de 5%
Obs.: RN (Regra de Negócio) para o Eletrônico Celular:
      O preço da diária corresponde ao preço base de locação acrescido de 10%

- Implemente:

1- Crie a superclasse abstrata Eletrônico
2- Crie o construtor com o atributo de instância marca §
3- Crie os métodos de instância get_marca e set_marca §
4- Crie o método abstrato preço da diária §
5- Crie um objeto da superclasse abstrata Eletrônico, teste § 
6- Crie o atributo de classe preço base de locação com valor fixo de R$ 100.00 §
7- Crie os métodos de classe get_preco_base e set_preco_base §
8- Crie a subclasse Televisao com o atributo marca. §
9- No construtor da subclasse, chame o construtor da superclasse e passe o marca §
10- Crie um objeto da subclasse Televisao, teste §
11- Sobrescreva o método abstrato da superclasse
    Obs.: RN (Regra de Negócio) para o Eletrônico econômico: §
    O preço da diária corresponde ao preço base de locação acrescido de 5%
12- Crie um objeto da subclasse Televisao, teste
13- Crie a subclasse Celular com o atributo marca.
14- No construtor da subclasse, chame o construtor da superclasse e passe o marca §
15- Crie um objeto da subclasse Celular, teste §
16- Sobrescreva o método abstrato da superclasse
    Obs.: RN (Regra de Negócio) para o Eletrônico Celular: §
    O preço da diária corresponde ao preço base de locação acrescido de 10%
17- Crie um objeto da subclasse Celular, teste

18- O sistema precisa informar a quantidade de Eletronicos cadastrados.
    Crie o atributo de classe para contar a quantidade de objetos criados.
19- Atualize o construtor para implementar esse requisito (funcionalidade).
20- Crie o método de classe para consultar a quantidade de Eletronicos
    cadastrados (instanciados). Teste
Prof. Barbosa
"""


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
    


    
