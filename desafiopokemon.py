import random

pokemon = {
    'bundaassada': {'ataque': 'bola de fogo','dano':35 },
    'jatodeagua': {'ataque': 'jato de agua', 'dano': 32},
    'carnemoida': {'ataque': 'chicote de carne','dano':30}
}


jogador1 = ''
jogador2 = ''

def selecionar_pokemon(jogador):
    print('selecione seu pokemon'.center(40, '-'))
    print(" (1) bundaassada \n (2) jatodeagua \n (3) carnemoida \n ")
    print('_'*40)
    escolha = int(input('escolha seu pokemon (1 ,2 ou 3): '))
    if escolha == 1:
        escolha = 'bundaassada'
    elif escolha == 2: 
        escolha = 'jatodeagua'
    elif escolha == 3: 
       escolha = 'carnemoida'
    else:
        print(f'não entendo isso seu bostacocopintinhoamarelotodomybrotherMYBESTOFREND❤️❤️❤️❤️❤️❤️❤️❤️😍😍😍😍😍😍😍❤️😍❤️💕❤️❤️😍❤️❤️❤️💕😘💕❤️😍❤️❤️💕😘💕💕😍❤️❤️❤️❤️😁😘😘💕❤️😍❤️❤️❤️💕😘😘💕❤️😍❤️❤️💕😘💕💕🤣❤️❤️😍😍❤️❤️❤️❤️❤️💕😘😘😍❤️')

    return escolha 

escolha1 = selecionar_pokemon(jogador1)
escolha2 = selecionar_pokemon(jogador2)

def ficha_habilidades(escolha):
    print(f'ficha de habilidade'.center(40, '-'))
    print(f'ataque: {pokemon[escolha]['ataque']} e Dano: {pokemon[escolha]['dano']}')
    
ficha_habilidades(escolha1)
print('-'*40)
ficha_habilidades(escolha2)

def dano_critico (escolha):
    dano_critico = pokemon[escolha]['dano'] * random.uniform(1,2)
    print(f'O dano_critico do {escolha} é de {dano_critico:.2f}')
    
d1 = dano_critico(escolha1)
d2 = dano_critico(escolha2)
print(f'o dano_critico do {escolha} é de')
#criem uma função chamado batalha (danocritico1, denocritico2)
def batalha (dano1, dano2):
  vida1 = 100 -  dano2
  vida2 = 100 - dano1

if vida1 > vida2:
      print(f' o vencedor é o player1 , vida restante {vida1:.2f}')
  print(f' o vencedor é o player2 , vida restante {vida2:.2f}')

batalha(d1,d2)
#cada pokemon tem 100 de vida 
#no final dessa batalha, mostre o vencedor