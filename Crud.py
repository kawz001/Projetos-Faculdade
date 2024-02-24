lista = []

def lista_nao_vazia():
    if lista != []:
        nao_vazia = True
    else:
        nao_vazia = False
        print('Lista vazia.')
    return nao_vazia

def menu():
    while True:
        print('[c] - Create')
        print('[r] - Read')
        print('[u] - Update')
        print('[d] - Delete')
        print('[e] - Exit')
        opcao = input('Opção: ').lower()
        if opcao == 'c' or opcao == 'r' or opcao == 'u' or opcao == 'd' or opcao == 'e' or opcao == 'l':
            break
        else:
            print('Opção inválida, tente novamente.')
    return opcao

       
def create():
    while True:
        nome = input('Nome: ')
        if nome == "" :
            break
        lista.append(nome.capitalize())

def read():
    lista.sort()
    for i in range(len(lista)):
        print((lista[i]))
    if len(lista) == 0:
        print('Não há nomes na lista.')
    ct = 0
    for nome in lista:
        print(ct, '-', nome)
        ct +=1

    
def update():
    '''nome_trocado = input('Insira o nome que você quer trocar: ')
    nome_novo = input('Insira um nome novo: ')
    for i in range(len(lista)):
        if lista[i].upper() == nome_trocado.upper():
            lista[i] = nome_novo.capitalize()
            break'''
    if lista != []:
        read()
        try:
            p = int(input('Insira a posição que você quer trocar:'))
            nome_novo1 = input('Insira o nome novo:')
            lista[p] = nome_novo1
        except IndexError as e:
            print('Posição não existe.\n', e)
        except Exception as e:
            print('Error Exception:\n', e)
    else:
        print('Lista Vazia')        


def delete():
    '''if lista != []:
        read()
        nome_removido = input('Insira um nome para ser removido da lista: ')
        if nome_removido in lista:
            lista.remove(nome_removido)
        else:
            (print('O nome não está na lista.'))       
    else:
        print('A lista está vazia.')'''
    if lista_nao_vazia():
        read()
        nome = input('Qual nome: ')
        if nome in lista:
            lista.remove(nome)
        else:
            print(f'O {nome} não está na lista.')

def clear():
    lista.clear()
    print('Sua lista foi limpada com sucesso.')

if __name__ == '__main__':
    while True:
        op = menu()
        if op == 'c' or op == 'C':
            create()
        elif op == 'r' or op == 'R':
            read()
        elif op == 'u' or op == 'U':
            update()
        elif op == 'd' or op == 'D':
            delete()
        elif op == 'l' or op == 'L':
            clear()
        elif op == 'e' or op == 'E':
            break
        #else:
           # print('Opção Inválida, tente novamente.')  