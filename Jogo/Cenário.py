from time import sleep


def Escolha():
    válido = False
    while not válido:
        entrada = str(input("Sua escolha: ")).strip()
        if entrada != '1' or entrada == '':
            if entrada != '2' or entrada == '':
                print(f'\033[:31mERRO: \"{entrada}\" não é uma escolha válida!\033[m')
            else:
                válido = True
                return int(entrada)
        else:
            válido = True
            return int(entrada)


def Ajudante(msg):
    print('-' * 50)
    sleep(1)
    print(f'\033[:35m{msg}\033[m')
    sleep(1)


def Protagonista(msg):
    print('-' * 50)
    sleep(1)
    print(f'\033[:33m{msg}\033[m')


def Opções(msg1, msg2):
    print('-' * 50)
    sleep(1)
    print('Perguntar:')
    print(msg1)
    print(msg2)


n1 = str(input('Qual seu nome [nick]: ')).title().strip()

Ajudante(f'Olá {n1} há quanto tempo!')
Opções('Quem é você?', 'Na verdade o que eu estou fazendo aqui?\n')

if Escolha() == 1:
    Protagonista('Quem é você ?')
    Ajudante('''Não sou alguém muito importante, mas estou aqui pra te ajudar
Vou te contar o por quê está aqui.
Mas depois, precisamos nos esconder!''')
    sleep(2)
    Ajudante('Pronto! Estamos bem, alguma dúvida?')
    Opções('Como vim parar aqui!', 'Do que nós estamos fugindo?')
    if Escolha() == 1:
        Ajudante('Você foi enviado pra nos Ajudar')
    else:
        Ajudante('')
else:
    Protagonista('Na verdade o que eu estou fazendo aqui?')
    Ajudante('Você corre perigo!')
