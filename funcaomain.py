#1 parte do codigo 
import random 

#@ criar estruturas de dados e as funções de suporte  
def aleatorio(n1, n2):
    return print(f'o numero aleatorio é: {random.randint(n1,n2)}')

#3 criando a função principal 
def main():
    numero1 = int(input("digite o 1 numero:  "))
    numero2 = int(input("digite o 2 numero:  "))
    aleatorio(numero1,  numero2)

#4 exucução da função principal 
if __name__ == "__main__":
    main()