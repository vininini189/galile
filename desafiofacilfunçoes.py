
lista_notas_champagnat = [2.5 , 2.9 , 0.2 , 2.9]

def calcular_media (lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    return print(f'a media das notas é de : {media}')

calcular_media(lista_notas_champagnat)

nome_do_aluno = input("digite sua media")
nota_do_aluno = float(input("parabens pela sua nota"))


def avaliar_aluno (nota_aluno, nome_aluno):
    if nota_aluno >= 9 and nota_aluno <= 10:
        print(f'parabéns, {nome_aluno}. excelente media!!!!!!!!!!!!!!!')
        avaliar_aluno(9, 'Nishi')

nome_do_aluno = input("digita sua nota ")
nota_do_aluno = float(input("tá media legal"))
        
if nota_aluno >= 7 and nota_aluno >= 8:
            print(f'parabens {nome_do_aluno} pelo menos vc esta na media né')
            
