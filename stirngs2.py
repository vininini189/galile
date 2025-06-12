#criem uma variavel chamada texto
#vINi FeS DEz 10 Anos

texto= "vIToR JUgO De 1X1x1x1X1X Nu aBANdOnadOS                                                                                                                                                                                          "


#VOU USAR COMAMDOS PARA MUDAR COISAS DO TEXTO DA VARIAVEL TEXTO

#metodos .capitalize () -> vai colocar todo o texto em  misnusculo com execeção a primeira letra dda frase
print(texto.capitalize())

#metodo .title() -> colocar em maiuscolo a primeira letra de toda palavra
print(texto.title())

#metodo .center(numero,caracter)
nome =  'vinicius'
print(nome.center(40, '-'))

#metodo len(variaveltexto) -> ele vai contrar quantos caracteres possui uma frase 
print(len(texto))

#metodo .lower() -> ele vai colocar todos as letras da frase em minuscula
print(texto.lower())

#metodo.upeer() -> ele vai colocar todos as letras da frase em maiuscula
print(texto.upper())

#metodos .replace(palavra antigo palavra nova)
frase= "vinicius é noob de forsake"
print(frase.replace('vinicius','joao luis'))