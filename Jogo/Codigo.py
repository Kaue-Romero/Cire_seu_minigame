from time import sleep


def Escolha():
    valido = False
    while not valido:
        entrada = str(input("Sua escolha: ")).strip()
        if entrada != '1' or entrada == '':
            if entrada != '2' or entrada == '':
                print(f'\033[:31mERRO: \"{entrada}\" não é uma escolha válida!\033[m')
            else:
                valido = True
                return int(entrada)
        else:
            valido = True
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


def Opcoes(msg1, msg2):
    print('-' * 50)
    sleep(1)
    print('Perguntar:')
    print(msg1)
    print(msg2)


n1 = str(input('Qual seu nome [nick]: ')).title().strip()
