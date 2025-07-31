estoque = (
    ("mouse lg tech", 10),
    ("mic hyper x", 5),
    ("acer nitro 5", 3),
    ("webcam hd", 0)
)

contador_zeros = 0 
soma = 0
print('produtos com menos de 5 unidades')
for i in estoque : #usei uma estrutura de laço para percorrer todos os itens da loja 
    if i[1] < 5: #verificaram se cada item tinha ou não 5 unidades
        print(f'- {i[0]}') #se a linha de cima é vdd, imprimir a quantidade 
    if i[1] == 0:
        contador_zeros += 1
    soma += i[1] #estou somando cada item da tupla estoque 
print(f'produtos esgotasos {contador_zeros}')
print(f'a soma dos produtos é: {soma}')




#programen a quantidade de itens zerados dentro da tupla estoque 