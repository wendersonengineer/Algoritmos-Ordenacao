
# HEAP SORT

def criar_heap(lista, tamanho_lista, indice_raiz):

    indice_maior = indice_raiz

    indice_esquerda = 2 * indice_raiz + 1

    indice_direita = 2 * indice_raiz + 2



    if indice_esquerda < tamanho_lista and lista[indice_esquerda] > lista[indice_maior]:
        indice_maior = indice_esquerda



    if indice_direita < tamanho_lista and lista[indice_direita] > lista[indice_maior]:
        indice_maior = indice_direita


    if indice_maior != indice_raiz:
        lista[indice_raiz], lista[indice_maior] = lista[indice_maior], lista[indice_raiz]
        criar_heap(lista, tamanho_lista, indice_maior)

def ordenar_por_heap_sort(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista // 2 - 1, -1, -1):
        criar_heap(lista, tamanho_lista, i)


    for i in range(tamanho_lista - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]

        criar_heap(lista, i, 0)

numeros_desordenados = [64, 43, 25, 12, 22, 11, 90]
ordenar_por_heap_sort(numeros_desordenados)
print(numeros_desordenados)







'''Heap Sort - É um algoritmo de ordenação baseado em uma estrutura de dados chamada Heap.
Ele ultiliza um heap binário para o rganizar os elementos e ordená-los.
Um heap é uma árvore binária onde o pai é sempre maior (heap máximo) ou menor (heap mínimo) do que seus filhos.
No Heap Sort, usamos o Heap máximo , garantindo que o maior número sempre fique na raiz da árvore e possa ser retirado sequencialmente para ordenação.

Vantagens

.Complexidade O(n log n) - Fnciona eficientemente para grandes listas.
.Ordenação dentro da própria lista - Não usa estrutura auxuliar, economizando memória.
.Garantia de desempenho consistente - Sempre funciona em tempo O(n log n), independentemente da entrada.
.Bom para sistemas onde a ordenação precisa ser feita diretamente sem memória extra.

Desvantagens

.Não é estável - Elementos iguais podem ter sua ordem original alterada.
.Pode ser mais lento que o Quick Sort na prática, devido ao número de comparações realizadas.
.Implementação mais complexa - Exige manipulação de dua estrutura heap binária '''