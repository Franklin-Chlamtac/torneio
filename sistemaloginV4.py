bancodedados = []
cadastro = {}
personagens = ['Anji', 'Axl', 'Chipp', 'Faust', 'Giovanna', 'Goldlewis', 'I-no', 'Jack-o', 'Ky', 'Leo',
               'May', 'Millia', 'Nagoriyuki', 'Potemkin', 'Ramlethal', 'Sol', 'Zato-1']
def cadastramento():
    usuario = str(input('Crie o seu login: '))
    cadastro['usuario'] = usuario
    senha = ' '
    senhaverificar = ''
    while senhaverificar != senha:
        senha = str(input('Crie uma senha:  '))
        senhaverificar = str(input('Repita sua senha.'))
        if senhaverificar != senha:
            print('Senhas não conhecidem, favor digitar novamente sua senha')
    cadastro['senha'] = senha
    nome = str(input('Digite seu nome:  '))
    cadastro['nome'] = nome
    cadastro['idade'] = str(int(input('Digite sua idade: ')))
    char = ' '
    while char not in personagens:
        char = str(input('Personagem utilizado: ').capitalize())
        if char not in personagens:
            print('Personagem não existe, por favor tente novamente.')
    cadastro['char'] = char

    # cadastras esses dados num banco de dados ficticio
    bancodedados.append(cadastro.copy())
    bdd = open(f'{usuario}_{senha}.txt', 'w')
    bdd.write(f"Parabéns, {nome}!\n")
    bdd.write(f"Cadastro já realizado, o torneio será realizado dia 30/02/2022\n")
    bdd.write(f"O personagem escolhido foi {char}!\n")
    bdd.write(f"Boa sorte!\n")
    bdd.close()
    print('=-' * 30, '=')
    print('CADASTRO FINALIZADO.')
    print('O torneio será realizado no dia 30/02/2022')
    print('Para acessar as informações do seu cadastro, por favor insira seu login e senha.')
    print('=-' * 30, '=')


def login():
    usuariologin = input('Digite seu usario: ')
    senhalogin = input('Digite sua senha:  ')

    arqv = open(f'{usuariologin}_{senhalogin}.txt')

    print('=-' * 30, '=')
    print(arqv.read())
    print('=-' * 30, '=')


