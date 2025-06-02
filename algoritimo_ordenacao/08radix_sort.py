
# RADIX SORT

def radix_sort(lista):
    maior_numero = max(lista)

    posicao_decimal = 1

    while maior_numero // posicao_decimal > 0:

        ordenar_por_contagem(lista, posicao_decimal)
        posicao_decimal *= 10

def ordenar_por_contagem(lista, posicao_decimal):

    tamanho_lista = len(lista)
    lista_ordenada = [0] * tamanho_lista
    contador = [0] * 10

    for numero in lista:
        indice_digito = (numero // posicao_decimal) % 10
        contador[indice_digito] += 1
        
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    for i in range(tamanho_lista -1, -1, -1):
        indice_digito = (lista[i]  // posicao_decimal) % 10
        lista_ordenada[contador[indice_digito] - 1] = lista[i]
        contador[indice_digito] -= 1
    
    for i in range(tamanho_lista):
        lista[i] = lista_ordenada[i]

numeros_desordenados = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(numeros_desordenados)
print(numeros_desordenados)







'''Radix Sort - Um algoritimo de ordenação baseado em dígitos, ou seja, ele ordena números olhando para cada casa decimal individualmente.
Ele usa Couting Sort como sub-algoritmo para organizar os números em diferentes posições, do dígigito  menos significativo ao mais significativo.
Funciona muito bem para números inteiros positivos, especialmente quando os valores possuem um limite supeior bem definido.

Vantagens

.Complexidade O(n) em casos favoráveis - Pode ser mais rápido que o Quick Sort em números inteiros longos.
Não depende de comparações diretas entre números, apenas organiza por dígitos.
Útil para ordenação de números grandes ou registros com múltiplos campos.

Desvantagens

.Não é adequadro para números de pontos flutuantes (float) sem modificações.
Exige mais memória para armazenar agrupamentos temporários.
Ineficiente para números curtos ou intervalos muito pequenos, onde outros métodos são melhores.
'''