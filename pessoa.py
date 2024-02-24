import datetime

class Pessoa:
    def __init__(self, a, b, c, d = 2000):
        self.nome = a
        self.peso = b
        self.altura = c
        self.ano_nascimento = d
    
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print('O nome inserido não é válido.')
    def get_ano_nascimento(self):
        return self.ano_nascimento
    def set_ano_nascimento(self, novo_ano):
        self.ano_nascimento = novo_ano
    def retorna_dados(self):
        dados = f'{self.nome}, {self.peso}, {self.altura}, {self.ano_nascimento}'
        return dados
    def __str__(self):
        s = f'{self.nome}, {self.peso}, {self.altura}, {self.ano_nascimento}'
        return s
    
    def calcula_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    def calcula_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.ano_nascimento
        return idade

if __name__ == '__main__':
    print()
    pessoa1 = Pessoa('Frederico', 57, 1.79, 2003)
    print('Objeto Criado:', pessoa1)
    pessoa2 = Pessoa('Fabrício', 60, 1.68)
    print('Objeto Criado:', pessoa2)

    print()
    print('- Dados pessoa 1:')
    print('Nome:', pessoa1.get_nome())
    pessoa1.set_nome('Jorje')
    print('Nome alterado:', pessoa1.get_nome())
    print('Ano de Nascimento:', pessoa1.get_ano_nascimento())
    pessoa1.set_ano_nascimento(2004)
    print('Ano de Nascimento Alterado:', pessoa1.get_ano_nascimento())
    print(f'Índice de massa corporal: {pessoa1.calcula_imc() :.2f} kg')
    print('Idade Pessoa 1:', pessoa1.calcula_idade())

    print('- Dados pessoa 2:')
    print('Nome:', pessoa2.get_nome())
    print('Ano de Nascimento:', pessoa2.get_ano_nascimento())
    print(f'Índice de massa corporal: {pessoa2.calcula_imc() :.2f} kg')
    print('Idade Pessoa 2:', pessoa2.calcula_idade())



