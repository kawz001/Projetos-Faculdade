class Veiculo(object):
    def __init__(self, modelo, ano, valor=0.00):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_ano(self):
        return self.ano
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('O valor não é válido.')

    def aumenta_valor(self, valor_aumento):
        valor_atual = self.valor
        valor_atualizado = valor_atual + valor_aumento
        self.valor = valor_atualizado
        
    def mostra_dados(self):
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)
        print('Valor:', self.valor)

    def retorna_dados(self):
        dados = f'{self.modelo}, {self.ano}, {self.valor}'
        return dados



if __name__ == '__main__':

    carro1 = Veiculo('HB', 2018, 60000.00)
    print('Objeto carro 1:', carro1)
    carro2 = Veiculo('Saveiro', 2013, 60000.00)
    print('Objeto carro 2:', carro2)

    print('- Dados Veículo 1:')
    retorno = carro1.get_modelo()
    print('Modelo:', retorno)
    print('Ano:', carro1.get_ano())
    print(f'Valor: R$ {carro1.get_valor() :.2f}')
    carro1.set_ano(2020)
    print('Ano atualizado:', carro1.get_ano())
    carro1.set_valor(20000)
    carro1.aumenta_valor(2000)
    print('Valor atualizado:', carro1.get_valor())


    print('- Dados Veículo 2:')
    carro2.set_modelo('BMW')
    retorno2 = carro2.get_modelo()
    print('Modelo:', retorno2)
    print('Ano:', carro2.get_ano())
    print(f'Valor: R$ {carro2.get_valor() :.2f}')   

    carro1.mostra_dados()
    carro2.mostra_dados()

    print('Veículo 1:', carro1.retorna_dados())
    print('Veículo 2:', carro2.retorna_dados())