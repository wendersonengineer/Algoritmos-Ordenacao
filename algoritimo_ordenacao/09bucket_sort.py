
#BUCKET SORT

def bucket_sort(lista):

    numero_baldes = len(lista)

    baldes = [[] for _ in range(numero_baldes)]

    for elemento in lista:
        indice_balde = min(numero_baldes -1,int(elemento * numero_baldes  / max(lista) + 1))

        baldes[indice_balde].append(elemento)
    
    for balde in baldes:
        balde.sort()

    lista_ordenada = []
    for balde in baldes:
        lista_ordenada.extend(balde)
    
    return lista_ordenada

numeros_desordenados = [10, 78, 5, 7, 2, 0, 89, 55]
numeros_ordenados = bucket_sort(numeros_desordenados)
print(numeros_ordenados)
    



'''Bucket Sort - Algoritmo de ordenação baseado na distribuição de valores em "baldes"(buckets).
Ele é muito eficiente quando os dados estão distribuídos uniformemente dentro de um intervalo conhecido.
O algoritimo organiza os elementos em diferentes baldes e então ordena cada balde inividualmente, normalmente usando Insertion Sort.

Vantagens

.Extremamente rápido para dados uniformemente distribuídos.
.Complexidade média O(n) - Melhor que outros algoritmos como Quick Sort e Merge Sort em certos casos.
.Pode ser usado para ordenação paralela - Cada balde pode ser processado independentemente.


Desvantagens

,Necessário definir previamente o número de baldes - O desempenho depende da escolha correta.
.Funciona melhor  para dados distribuídos de forma uniforme - Caso contrário, os baldes podem ficar desbalanceados.
.Consome memória extra -  Precissa armazenar os baldes temporariamente.'''