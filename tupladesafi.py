pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]
soma_produtos_entregues = []
#somar valor de todos os produtos entregues
for i in pedidos : 
    if i[3] == 'Entregue' : 
        soma_produtos_entregues.append(i[2])

    print(f'a soma todos os produtos entregues é : {sum(soma_produtos_entregues)}')
  
print('protutos entregues'.center(40,'-'))
for i in pedidos: 
    if i[3] == 'Entregue':
        print(f' -  {i[0]}')

#percorrer a lista de pedidos
#averificar se a categoria está como vestuária e se o  status 

soma_cancelado_vestuario = 0 

for i in pedidos: #percorerrendo a lista de pedidos 
    if i[3] == 'Cancelado' and i[1] == 'Vestuário' : 
            soma_cancelado_vestuario += 1 #soma 1 do valor antigo da variável soma_cancelado_vesturio
print(f'Cancelado_cancelado da categoria vestuário:{soma_cancelado_vestuario}')


filtro = input('Digite uma categoria para filtra:  ')

for i in pedidos: 
     if filtro == i[1]:
          print(f'- {i[0]}')

