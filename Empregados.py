class Funcionario():
    def __init__(self, cpf, nome, salario = 0.0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario
    
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cof = novo_cpf

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if type(novo_salario) in (int, float):
            self.salario = novo_salario
        else:
            print('O número inserido não é válido.')

    def __str__(self):
         s = f'CPF: {self.cpf}, Nome: {self.nome}, Salario: {self.salario}'
         return s

class Gerente(Funcionario):
    def __init__(self, cpf, nome, salario, senha, func):
            super().__init__(cpf, nome, salario)
            self.senha = senha
            self.func = func
#    def get_cpf(self):
#        return self.cpf
#    def set_cpf(self, novo_cpf):
#        self.cof = novo_cpf

#    def get_nome(self):
#        return self.nome
#    def set_nome(self, novo_nome):
#        self.nome = novo_nome

#    def get_salario(self):
#        return self.salario
#    def set_salario(self, novo_salario):
#        if type(novo_salario) in (int, float):
#            self.x = novo_salario
#        else:
#            print('O número inserido não é válido.')

    def get_senha(self):
        return self.senha
    def set_senha(self, nova_senha):
        self.senha = nova_senha
    def autentica(self):
        senhas = input('Insira sua senha:')
        if senhas == self.senha:
            print('Senha Correta.')
            return True
        else:
            print('Acesso negado, senha incorreta.')
            return False

    
    def get_func(self):
        return self.func
    def set_func(self, novo_func):
        if type(novo_func) in (int, float):
            self.func = novo_func
        else:
            print('O número de funcionários inserido não é válido.')

    def __str__(self):
         s = f'CPF: {self.cpf}, Nome: {self.nome}, Salario: {self.salario}, Senha: {self.senha}, Nº de Funcionários: {self.func}'
         return s
    
    def bonificacao(self):
        valor = self.salario * 0.10
        return valor
    

if __name__ == '__main__':
    g1 = Gerente('987', 'Luíz', 10000.00,'senha123', 3)
    print(g1)
    f1 = Funcionario('123', 'Paulo, 1000.00')
    print(f1)
    f2 = Funcionario('456', 'João')
    print(f2)
