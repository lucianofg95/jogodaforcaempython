import os

def menu():
    print("JOGO DA FORCA - CURSO PYTHON")
    print("Escolha a Opção:")
    print("1) Iniciar")
    print("2) Placar")
    print("3) Sair")
    op = input("Escolha o número da opção: ")
    return op


def layout_palavra(acertos, palavra_secreta):
    os.system("clear")
    print()
    for acerto, letra in zip(acertos, palavra_secreta):
        if acerto: # quer dizer que se o acerto for igual a True
            print(letra.upper(), end=' ')
        else: #se o acerto for falso
            print('_', end=' ')
    print()


def update_acertos(palavra_secreta, chute, acertos):
    for i, letra in enumerate(palavra_secreta):
        if chute.lower() == letra:
            acertos[i] = True


def setup():
    palavra_secreta, dica = cria_palavra_dica()
    n_letras = len(palavra_secreta)
    acertos = [False]*n_letras
    return palavra_secreta.lower(), dica, n_letras, acertos


def jogar():

    os.system("clear")

    palavra_secreta, dica, n_letras, acertos = setup()
    tentativas = 0

    while tentativas < 5:

        layout_palavra(acertos, palavra_secreta)
        print('DICA SECRETA: %s' % dica)
        chute = input('\ntente uma letra: ')

        update_acertos(palavra_secreta, chute, acertos)

        if chute not in palavra_secreta:

            tentativas += 1
            if tentativas == 1:
                enforcado02(q=0,w=1,e=0,r=0,t=0,y=0)
            elif tentativas ==2:
                enforcado02(q=0,w=2,e=0,r=0,t=0,y=0)
            elif tentativas ==3:
                enforcado02(q=0,w=3,e=0,r=0,t=0,y=0)
            elif tentativas ==4:
                enforcado02(q=0,w=3,e=4,r=6,t=0,y=0)
            else:
                enforcado02(q=0,w=3,e=4,r=6,t=7,y=11)

            if tentativas == 5:

                layout_palavra(acertos, palavra_secreta)
                print('ACABARAM AS TENTATIVAS!!!')
                enforcado()
                forca_python()

        if all(acertos):

            layout_palavra(acertos, palavra_secreta)
            print("PARABÉNS, VOCÊ GANHOU!!!")

            forca_python()


def cria_palavra_dica():
    os.system("clear")
    palavra_secreta = input("\nigite a palavra secreta: ")
    dica = input("\nDigite a dica: ")
    return palavra_secreta, dica


def forca_python():
    os.system("clear")
    op = int(menu())
    if op == 1:
        jogar()
    elif op == 2:
        print('TAREFA PARA VOCÊ FAZER')
    else:
        print('sair')

def enforcado():
    box = ['\u2572']
    a = [' ', ' ', box[0], ' ', '/']
    b = ['|', '|', '0', '|', ' ']
    c = [' ', ' ', '/----{sorry!!!}', '', box[0]]
    for boneco in zip(a, b, c):
        print(''.join(boneco))

def enforcado02(q,w,e,r,t,y):
    box = [' \u2572']
    membros = [box[0], '0', '/', '', '', ' |', '', '', '/', box[0]]
    print(''.join(membros[q:w]), '\n', ''.join(membros[e:r]), '\n', ''.join(membros[t:y]))

forca_python()
