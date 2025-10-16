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
    
dano_critico(escolha1)
dano_critico(escolha2)