import random

def selecionar_pokemon():
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
    
    elif print( digite um numero de 1,2 ou 3 ): 


selecionar_pokemon():

pokemon = {
    'bundaassada': {'ataque': 'bola de fogo','dano':35 },
    'jatodegua': {'ataque': 'jato de agua', 'dano': 32},
    'carmemoida': {'ataque': 'chicote de carne','dano':30}
}