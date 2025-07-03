notas = [      
    ["ana", [8, 7, 9]],
    ["carlos", [5, 6, 7]],
    ["joão", [10, 9, 8]],
]

for aluno in notas: 
    nome_aluno = aluno[0]
    media = sum(aluno[1]) / len(aluno)

    print(f'a media do aluno {nome_aluno} é de {media}')