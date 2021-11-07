import random
import forca

def alterar_pontuacao(pontos,pontos_perdidos):
    pontos = pontos - pontos_perdidos
    return pontos

def jogar():

    imprimir_mensagem()
    numero_secreto = definir_numero_secreto()
    total_de_tentativas = definir_nivel()
    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            imprime_mensagem_vencedor(pontos)
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = alterar_pontuacao(pontos,pontos_perdidos)

    if(not acertou):
        imprime_mensagem_perdedor(numero_secreto)
    finalizar_jogo()


def imprimir_mensagem():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def definir_numero_secreto():
    numero_secreto = random.randrange(1, 101)
    return numero_secreto

def definir_nivel():
    total_de_tentativas = 0
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    return total_de_tentativas

def imprime_mensagem_vencedor(pontos):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

    print("\n Sua pontuação: {} '\\0/'".format(pontos))

def imprime_mensagem_perdedor(numero_secreto):
    print("Puxa, você perdeu!")
    print("O número secreto era {}".format(numero_secreto))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def finalizar_jogo():
    print("O que deseja fazer?")
    print("(1) Repertir o jogo   (2) Jogar o 'Jogo da Forca'   (3) Finalizar o jogo")
    escolha = int(input(">> "))

    if(escolha == 1):
        jogar()
    elif(escolha ==2):
        forca.jogar()
    else:
        print("Obrigado por jogar. Até a próxima vez!!!!")

if(__name__ == "__main__"):
    jogar()
