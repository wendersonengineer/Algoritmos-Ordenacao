
# INSERTION SORT

def insertion_sort(lista):

    tamanho_lista = len(lista)

    for indice_atual in range(1, tamanho_lista):

        elemento_chave = lista[indice_atual]

        posicao = indice_atual - 1

        while posicao >= 0  and lista[posicao] > elemento_chave:

            lista[posicao + 1] = lista[posicao]
            posicao-= 1

        lista[posicao + 1] = elemento_chave

numeros = [10, 2, 4, 5, 1, 3, 20, 87, 52, 54,  15]
insertion_sort(numeros)
print("Lista ordenada")
print(numeros)

'''Insertion Sort - Algoritmo de ordenação por inserção

Vantagens:
.Simples de entender e implementar.
.Eficiente para listas pequenas ou quase ordenadas.

Desvantagens:

.Complexidade O(n²) no pior caso, tornando-o lento para listas grandes.
.Ineficientes para grandes conjuntos de dados em comparação com algoritimos mais avançados.'''

