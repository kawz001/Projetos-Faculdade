class Computador:
    def __init__(self, x, y, z):
        self.placa = x
        self.ram = y
        self.processador = z
    def get_placa(self):
        return self.placa
    def set_placa(self, nova_placa):
        self.placa = nova_placa
    def get_ram(self):
        return self.ram
    def set_ram(self, nova_ram):
        self.ram = nova_ram
    def get_processador(self):
        return self.processador
    def set_processador(self, novo_processador):
        self.processador = novo_processador
    
    def retorna_dados(self):
        dados = f'{self.get_placa()}, {self.get_ram()}, {self.get_processador()}'
        return dados

if __name__ == '__main__':
    computador1 = Computador('GTX 1650', '8 GB' , 'i5')
    print(computador1)

    computador2 = Computador('GTX 2080', '16 GB', 'i7')
    print(computador2)

    computador3 = Computador('GTX 3090', '32 GB', 'i9')
    print(computador3)

    #Outra maneira chamando os métodos "Set":
    '''
    print('- Computador 1:')
    print('Placa:', computador1.get_placa())
    print('Memória RAM:', computador1.get_ram())
    print('Processador:', computador1.get_processador())
    computador1.set_placa('GTX 1650')
    computador1.set_ram('8 GB')
    computador1.set_processador('i5')
    print('Nova placa:', computador1.get_placa())
    print('Nova memória RAM:', computador1.get_ram())
    print('Novo processador:', computador1.get_processador())

    print('- Computador 2:')
    print('Placa:', computador1.get_placa())
    print('Memória RAM:', computador1.get_ram())
    print('Processador:', computador1.get_processador())
    computador2.set_placa('GTX 2080')
    computador2.set_ram('16 GB')
    computador2.set_processador('i7')
    print('Nova placa:', computador2.get_placa())
    print('Nova memória RAM:', computador2.get_ram())
    print('Novo processador:', computador2.get_processador())

    print('- Computador 3:')
    print('Placa:', computador1.get_placa())
    print('Memória RAM:', computador1.get_ram())
    print('Processador:', computador1.get_processador())
    computador2.set_placa('GTX 3090')
    computador2.set_ram('32 GB')
    computador2.set_processador('i9')
    print('Nova placa:', computador3.get_placa())
    print('Nova memória RAM:', computador3.get_ram())
    print('Novo processador:', computador3.get_processador())
    '''
    print('Dados computador 1:', computador1.retorna_dados())
    print('Dados computador 2:', computador2.retorna_dados())
    print('Dados computador 3:', computador3.retorna_dados())