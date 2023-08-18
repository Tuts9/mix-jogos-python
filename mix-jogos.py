import random
from time import sleep
print('\033[34mSEJA BEM VINDO AO SEU PROGRAMA DE JOGOS\033[0m')
sleep(1.5)
print('Escolha 1 para jogar o jogo da ADIVINHAÇÃO ou escolha 2 para jogar o jogo do JOKENPÔ')
sleep(1.5)
escolhaInicio = int(input('Digite o número referente a sua escolha '))
if escolhaInicio == 1:
    computador = random.randint(0, 10)
    print('Sou seu computador, acabei de pensar em um número entre 0 e 10')
    print('Será que vai acertar?')
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input('Qual é seu palpite? '))
        palpites += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Mais...Tente novamente')
            else:
                print('Menos...Tente novamente')
    print(f'Acertou, Você precisou de {palpites} tentativas.')
elif escolhaInicio == 2:
    print('\033[32mVAMOS BRINCAR DE PEDRA, PAPEL, TESOURA\033[0m')
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = random.randint(0, 2)
    print('''\033[32mSuas opções
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA\033[0m''')
    sleep(2)
    jogador = int(input('Qual a sua jogada? '))

    print('JO..')
    sleep(1)
    print('KEN..')
    sleep(1)
    print('PÔ')
    sleep(1.5)

    print(f'O computador escolheu {itens[computador]}')
    print(f'O jogador escolheu {itens[jogador]}')
    if computador == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('Jogador venceu!')
        elif jogador == 2:
            print('Computador venceu.')
    elif computador == 1:
        if jogador == 0:
            print('Computador venceu.')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Jogador venceu!')
    elif computador == 2:
        if jogador == 0:
            print('Jogador venceu!')
        elif jogador == 1:
            print('Computador venceu.')
        elif jogador == 2:
            print('Empate')
