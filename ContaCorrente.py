
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
