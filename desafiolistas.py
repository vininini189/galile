arenas =  [
    [1200, 1500, 1100, 1800, 1700], # arena 1
    [1000, 950, 1100, 1050, 980],   # arena 2
    [2000, 1900, 1950, 2100, 2200], # arena 3
]

contador = 0 
lista_medias = []



#criei um laço para precorrer a lista arenas 
for a in arenas: #'para cada a (arena) dentro da lista arenas
      contador += 1 #estou somando 1 do  antigo valor do variavel contador 
      media_arenas = sum(a) / len(a)
      lista_medias.append(media_arenas) #adicinando a media calculada na lista_medias
      print(f'a media da arena {contador} é de: {media_arenas}')
      print(lista_medias)

print(f'a maior pontuação entre as arenas é de: {max(lista_medias)}')