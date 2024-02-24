ct_masc = 0
ct_fem = 0
maior = 0
menor = 3
print("Use [K] para finalizar o programa.")

while True:
    var = input('Insira o gênero, sendo [m] para masculino e [f] para feminino:')
    if var == 'K' or var == 'k':
        break
    if var == 'm' or var == 'M':
        ct_masc = ct_masc + 1
    elif var == 'f' or var == 'F':
        ct_fem = ct_fem + 1
    alt = float(input('Insira a altura:'))
    if alt > maior:
        maior = alt
    if alt < menor:
        menor = alt

print('Quantidade Masculina:', ct_masc)
print('Quantidade Feminina:', ct_fem)
print('Maior altura:', maior)
print('Menor altura:', menor)