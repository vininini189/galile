arenas =  [
    [1200, 1500, 1100, 1800, 1700], # arena 1
    [1000, 950, 1100, 1050, 980],   # arena 2
    [2000, 1900, 1950, 2100, 2200], # arena 3
]

for arena in arenas: 
    
    arenas_medias = sum(arena[1]) / len(arena)

    print(f'a arenas do arena {arenas_medias} é de {arenas}')