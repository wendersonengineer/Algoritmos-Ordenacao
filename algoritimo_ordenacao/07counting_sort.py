
# COUNTING SORT

def couting_sort(lista):

    if len(lista) == 0:
        return lista
    
    valor_maximo = max(lista)

    contador = [0] * (valor_maximo + 1)

    for numero in lista:
        contador[numero] += 1

    lista_ordenada = []
    for indice, quantidade in enumerate(contador):
        lista_ordenada.extend([indice] * quantidade)
    
    return lista_ordenada
    
numeros_desordenados = [4, 2, 2, 8, 3, 3, 1, 4]
numeros_ordenados = couting_sort(numeros_desordenados)
print(numeros_ordenados)






'''Counting Sort - Algoritmo de ordenação baseado na contagem de ocorrências de cada elemento.
Ele funciona bem quando os elementos da lista estão dentro de um intervalo pequeno e conhecido.
Diferente de outros Algoritimos, nào compara elementos, apenas os organiza com base em sua frequências.

Vantagens

.Muito rápido para intervalos pequenos - Complexidade O(n + k), onde k é o maior valor da lista.
.Oredenação linear quando k é pequeno - Pode ser mais rápido que o Quick Sort e Merge Sorte em certos casos.
.Boa escolha para ordenação de números inteiros pequenos ou dados categóricos.

Desvantagens

.Consome memória extra para armazenar contagens - Ineficiente para intervalor grandes (k muito alto).
Não é adequadro para dados com números reais (float) - Apenas para inteiros.
Não é um algoritimo de ordenação comparativa - Usa abordagem baseada em frequência.'''