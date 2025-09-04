loja_games  = {
    "Minecraft" : {"Preço" : 59.90, "Estoque": 5},
    "Fifa" : {"Preço" : 199.90, "Estoque": 3},
    "God of war" : {"Preço" : 149.90, "Estoque": 4},
}

carrinho = {}


for jogo, info in loja_games.items():
    print(f' jogo: {jogo} - Preço: {info['Preço']} - Estoque: {info['Estoque']}')
    
print("-" * 50)

while True:
    escolha_cliente = input("qual jogo vc deseja pedaço de coco ? (digite 'sair' para finalizar) :").capitalize().strip()
    if escolha_cliente == 'sair':
        break 
    escolha_cliente = (input("oq vc vai querer comprar na loja do vininini189")).strip().capitalize()
    
    #verificando se existe o jogo
    if escolha_cliente in loja_games:
        print("o jogo está disponivel:AGORA VC VAI TER QUE COMPRAR")
        vitor_legalmaschato = int(input("Quantas unidades você querer coco eletronico ?"))
        if vitor_legalmaschato >= loja_games[escolha_cliente]['Estoque']:
            print("NÃO TEM ESTOQUE SEU ANIMAL")
        else : #cenario onde tem estoque disponivel, vamos subtrair a quantidade do dicionario loja games
            loja_games[escolha_cliente]['Estoque'] -= vitor_legalmaschato
            carrinho[escolha_cliente] = vitor_legalmaschato
            print('obr pelo dinheiro otario a compra tá pronta vc vai querer mais algo ou n ')

    else:
        print("o jogo não está disponivel; SAIA DA QUI")

    print(carrinho)
    print(f'O estoque atual do jogo escolha é esse seu burro {loja_games[escolha_cliente]['Estoque']}')

total = 0
print('resumo da compra'.center(40, '-'))
for jogo, qtd in carrinho.items():
    Preço = loja_games[jogo]["Preço"]
    total += Preço * qtd
    print(f'{jogo} x {qtd}'.centre(40))
print('-'*40)
print(f'Total: RS {total.center}.center(40)')