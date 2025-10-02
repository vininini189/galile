
lista_notas_champagnat = [2.5 , 2.9 , 0.2 , 2.9]

def calcular_media (lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    return media

calcular_media(lista_notas_champagnat)

nome_do_aluno = input("digite sua o nome do aluno: ")
nota_do_aluno = calcular_media(lista_notas_champagnat)

def avaliar_aluno (nota_aluno, nome_aluno):
    if nota_aluno >= 9 and nota_aluno <= 10:
        print(f'parabéns, {nome_aluno}. excelente media!!!!!!!!!!!!!!!')

    if nota_aluno >= 7 and nota_aluno <= 8.9:
        print(f'Foi, {nome_aluno}. Passou!!!!!!!!!!!!!!!!')

    if nota_aluno >= 5 and nota_aluno <= 6.9:
        print(f'Tome cuidado, {nome_aluno}. Quase não passou!!!!!!!!!!!!!!!!')

    if nota_aluno >= 0 and nota_aluno <= 5:
        print(f'Passou não! {nome_aluno}')

avaliar_aluno(nota_do_aluno, nome_do_aluno)

            
