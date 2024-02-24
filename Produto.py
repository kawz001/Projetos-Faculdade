class Produto:
    def __init__(self, a = ' ', b = 0, c = 0, d = 0, e = 0):
        self.nome = a
        self.compra = b
        self.venda = c
        self.estoque = d
        self.minima = e

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print('O nome inserido não é válido.')

    def get_estoque(self):
        return self.estoque
    def set_estoque(self, novo_estoque):
        if novo_estoque != 0 :
            self.estoque = novo_estoque
        else:
            print('O valor digitado não é válido.')
    def atualiza_estoque(self, qtd_vendida):
        self.estoque -= qtd_vendida
    def repor_produto(self, qtd_adquirida):
        self.estoque += qtd_adquirida
           
    def get_minima(self):
        return self.minima
    def set_minima(self, nova_minima):
        self.minima = nova_minima
    def alerta_estoque(self):
        if self.estoque < self.minima:
            return True
        else:
            return False

    def get_compra(self):
        return self.compra

    def set_compra(self, nova_compra):
        if nova_compra != 0:
            self.compra = nova_compra
        else:
            print('O valor não é válido.')
    
    def set_lucro(self):
        lucro = self.venda - self.compra
        return lucro
    
    def __str__(self):
        s = f'{self.nome}, {self.compra}, {self.venda}, {self.estoque}, {self.minima}'
        return s

if __name__ == '__main__':
    produto1 = Produto('Arroz', 19.00, 27.50, 67, 20)
    print(produto1)
    produto2 = Produto('Mandioca')
    print(produto2)
    produto3 = Produto('Frango', 30.00)
    print(produto3)

    print()
    print('- Dados Produto 1:')
    produto1.set_nome('Feijão')
    print('Nome Atualizado:', produto1.get_nome())
    produto1.set_compra(20.00)
    print('Valor compra atualizado:')
    produto1.set_estoque(60)
    print('Estoque atualizado:', produto1.get_estoque())
    print()

    print('- Dados Produto 2:')
    print('Nome:', produto2.get_nome())
    print('Valor de Compra:', produto2.get_compra())
#    print('Valor de Venda:', produto2.get_venda())
#    print('Quantidade no Estoque:', produto2.get_estoque)
    #print('Quantidade Mínima de Estoque:', produto2.get_minima())
    print()

    print('- Dados Produto 3:')
    print('Nome:', produto3.get_nome())
#    print('Valor de Compra:', produto3.get_compra())
#   print('Valor de Venda:', produto3.get_venda())
#    print('Quantidade no Estoque:', produto3.get_estoque)
#   print('Quantidade Mínima de Estoque:', produto3.get_minima())
