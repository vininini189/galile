loja_games  = {
    "Minecraft" : {"Preço" : 59.90, "Estoque": 5},
    "Fifa23" : {"Preço" : 199.90, "Estoque": 3},
    "God of war" : {"Preço" : 149.90, "Estoque": 4},
}

for jogo, info in loja_games.items():
    print(f' jogo: {jogo} - Preço: {info['Preço']} - Estoque: {info['Estoque']}')
    
escolha_cliente = (input("oq vc vai querer comprar na loja do vininini189")).strip().capitalize()

#verificando se existe o jogo
if escolha_cliente in loja_games:
    print("o jogo está disponivel:AGORA VC VAI TER QUE COMPRAR")
    vitor_legalmaschato = int(input("Quantas unidades você querer coco eletronico ?"))
    if vitor_legalmaschato >= loja_games[escolha_cliente]['Estoque']:
        print("NÃO TEM ESTOQUE SEU ANIMAL")

else:
    print("o jogo não está disponivel; SAIA DA QUI")