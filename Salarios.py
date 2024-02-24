from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, idade, salario, dias=3):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.dias = dias

    @abstractmethod
    def calcular_bonus(self):
        pass
    
    def dias_trabalho(self):
        pass

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        if salario >= 0:
            self.salario = salario
        else:
            print('Salário não pode ser negativo.')
    
    def get_dias(self):
        return self.dias

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.get_salario() * 0.3
    
    def dias_trabalho(self):
        return self.get_dias() + 1

class Programador(Funcionario):
    def calcular_bonus(self):
        return self.get_salario() * 0.2
    def dias_trabalho(self):
        return self.get_dias() + 2

if __name__ == '__main__':

    gerente1 = Gerente('Larissa', 35, 8000.0)
    programador1 = Programador('Caio', 28, 5000.0)

    gerente1.set_nome('Fernanda')
    gerente1.set_idade(36)
    gerente1.set_salario(8500.0)

    programador1.set_nome('Kaio')
    programador1.set_salario(5500.0)
    programador1.set_idade(29)


    print(f'{gerente1.get_nome()} - Idade: {gerente1.get_idade()} - Salário: R$ {gerente1.get_salario():.2f}')
    print(f'Bonus Gerente: R$ {gerente1.calcular_bonus():.2f}')
    print(f'Dias trabalhados por semana: {gerente1.dias_trabalho()}')

    print(f'{programador1.get_nome()} - Idade: {programador1.get_idade()} - Salário: R$ {programador1.get_salario():.2f}')
    print(f'Bonus Programador: R$ {programador1.calcular_bonus():.2f}')
    print(f'Dias trabalhados por semana: {programador1.dias_trabalho()}')