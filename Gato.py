import datetime

class Gato:
    def __init__(self, a = 'Jorjin', b = 2022, c = 'Preto'):
        self.nome = a
        self.ano_nascimento = b
        self.cor = c
    
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
    def get_cor(self):
        return self.cor
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    def retorna_dados(self):
        dados = f'{self.nome}, {self.ano_nascimento}, {self.cor}'
        return dados
    def __str__(self):
        s = f'{self.nome}, {self.ano_nascimento}, {self.cor}'
        return s
    
    def calcula_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.ano_nascimento
        return idade
    def transforma_idade(self):
        idade_gato = self.calcula_idade() * 14
        return idade_gato

if __name__ == '__main__':
    print()
    gato1 = Gato('Frederico', 2018, 'Laranja')
    print('Objeto Criado:', gato1)
    gato2 = Gato('Fabrício', 2021)
    print('Objeto Criado:', gato2)
    gato3 = Gato('Guts')
    print('Obejto Criado:', gato3)
    gato4 = Gato()
    print('Objeto Criado:', gato4)

    print()
    print('- Dados gato 1:')
    print('Nome:', gato1.get_nome())
    gato1.set_nome('Carlinho')
    print('Nome alterado:', gato1.get_nome())
    print('Ano de Nascimento:', gato1.get_ano_nascimento())
    gato1.set_ano_nascimento(2020)
    print('Ano de Nascimento Alterado:', gato1.get_ano_nascimento())
    print('Idade gato 1:', gato1.calcula_idade())
    print('Idade equivalente à humana:', gato1.transforma_idade())
    print('Cor do gato:', gato1.get_cor())
    print('Dados:', gato1.retorna_dados())
    print()

    print('- Dados gato 2:')
    print('Nome:', gato2.get_nome())
    print('Ano de Nascimento:', gato2.get_ano_nascimento())
    print('Idade gato 2:', gato2.calcula_idade())
    print('Idade equivalente à humana:', gato2.transforma_idade())
    print('Cor do gato:', gato2.get_cor())
    gato2.set_cor('Preto e Branco')
    print('Cor do gato alterada:', gato2.get_cor())
    print('Dados:', gato2.retorna_dados())
    print()

    print('- Dados gato 3:')
    print('Nome:', gato3.get_nome())
    print('Ano de Nascimento:', gato3.get_ano_nascimento())
    print('Idade gato 3:', gato3.calcula_idade())
    print('Idade equivalente à humana:', gato3.transforma_idade())
    print('Cor do gato:', gato3.get_cor())
    print('Dados:', gato3.retorna_dados())
    print()

    print('- Dados gato 4:')
    print('Nome:', gato4.get_nome())
    print('Ano de Nascimento:', gato4.get_ano_nascimento())
    print('Idade gato 4:', gato4.calcula_idade())
    print('Idade equivalente à humana:', gato4.transforma_idade())
    print('Cor do gato:', gato4.get_cor())
    print('Dados:', gato4.retorna_dados())



    


