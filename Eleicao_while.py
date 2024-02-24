lista_voto = []
print('Digite [-1] para finalizar')

while True:
    voto = int(input('Insira seu voto, sendo\n1 - Candidato 1\n2 - Candidato 2\n3 - Candidato 3\n5 - Nulo\n6 - Branco\nInsira:'))
    if voto == -1:
        break
    lista_voto.append(voto)
print('Votos Candidato 1:', lista_voto.count(1))
print('Votos Candidato 2:', lista_voto.count(2))
print('Votos Candidato 3:', lista_voto.count(3))
print('Votos Nulos:', lista_voto.count(5))
print('Votos em Branco:', lista_voto.count(6))