"""                 Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Com base nos conceitos de Programação Orientada a Objetos (POO)
e inheritance (herança), implemente a entidade conta corrente com as
especificidades de conta corrente de uma pessoa física e de uma pessoa
jurídica.
Levante as características comuns e as características
específica de uma conta corrente de pessoa física e de conta corrente
de pessoa jurídica.

- Algumas características de uma conta corrente:
nome, saldo, gênero, CPF, modalidade de PJ e CNPJ

- Implemente estes itens:

1- Crie a superclasse Conta
2- Crie o método construtor com os atributos nome e saldo, teste
3- Crie os métodos gets e sets da superclasse, teste
4- Sobrescreva o método __str__ para ele retornar os atributos, teste
5- Crie a subclasse Conta pessoa física
6- Crie o método construtor com os atributos nome, saldo, genero e cpf
7- Crie uma instância (objeto) de Conta_PF, teste
8- Crie os métodos get e set
9- Use os métodos da subclasse Conta_PF
10- Use o método do Python vars.              Sintaxe: print(vars(objeto))
11- Use o método do Python __dict__                    print(objeto.__dict__)
12- Crie a subclasse Conta pessoa jurídica
13- Crie o método construtor com os atributos nome, saldo, modalidade e cnpj
14- Crie uma instância (objeto) de Conta_PJ
15- Crie os método get e set, teste
16- Crie o método deposito, ele recebe o valor do depósito e atualiza o saldo, teste
17- Crie o método retirada, ele recebe o valor da retirada e atualiza o saldo, teste
18- Refaça o método retirada usando RNs (Regras de Negócios) bancárias. Teste
Prof. Barbosa
"""
class Conta(object):
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def deposita(self, v):
        self.saldo = self.saldo + v
    
    #def saque(self, saq):
    #    self.saldo = self.saldo - saq

    def saque_rn(self, saq):
        if self.__class__ == 'ContaPf':
            if saq > self.saldo:    
                print('Saldo insuficiente.')
            else:
                self.saldo -= saq - 2
        else:
            if saq > self.saldo:
                print('Saldo insuficiente.')
            else:
                self.saldo = self.saldo - 5
            

    def __str__(self):
        s = f'Nome: {self.nome}, R$ {self.saldo}'
        return s    
class ContaPf(Conta):
    def __init__(self, nome, genero, cpf, pj, cnpj, saldo = 0.0):
        super().__init__(nome, saldo = 0.0)
        self.nome = nome
        self.saldo = saldo
        self.genero = genero
        self.cpf = cpf
        self.pj = pj
        self.cnpj = cnpj

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_genero(self):
        return self.genero
    def set_genero(self, novo_genero):
        self.genero = novo_genero

    #def saque_1(self, v1):
    #    self.saldo = self.saldo - v1  - 2

class ContaPj(Conta):
    def __init__(self, nome, saldo, pj, cnpj):
        super().__init__(nome, saldo = 0.0)
        self.saldo = saldo
        self.pj = pj
        self.cnpj = cnpj

    #def saque_2(self, v2):
    #    self.saldo = self.saldo - v2 - 5
    

if __name__ == '__main__':
    c = Conta('Alice', 8.00)
    print(c)
    print('- Superclasse:\nNome:', c.get_nome())
    print('Saldo:', c.get_saldo())
    c.set_nome('Emily')
    print('Novo nome:', c.get_nome())
    print(vars(c))
    print(c.__dict__)
    c1 = ContaPf('João','Masculino', 1,  'Micro', 1,  2000.00)
    print(c1)
    print(vars(c1))
    print(c1.__dict__)
    c2 = ContaPj('Paulo', 3000, 'Micro', 3)
    print(c2)
    print(vars(c2))
    print(c2.__dict__)
    #c.deposita(v = float(input('Insira um valor para depositar:')))
    c1.saque_1(v1 = float(input('Insira um valor para sacar (Pessoa Física):')))
    print(c1)
    c2.saque_2(v2 = float(input('Insira um valor para sacar (Pessoa Jurídica):')))
    print(c2)
    #c.saque(saq = float(input('Insira um valor para sacar:')))
    #print(c)
