
# QUICK SORT

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        elemento_pivo = lista[len(lista) // 2]

        menores = [x for x in lista if x < elemento_pivo]
        iguais = [x for x in lista if x == elemento_pivo]
        maiores = [x for x in lista if x > elemento_pivo]

        return quick_sort(menores) + iguais + quick_sort(maiores)
    
numeros = [64, 43, 25, 12, 22, 11, 90]
numeros_ordenados = quick_sort(numeros)
print(numeros_ordenados)





'''Quick Sort - Algoritmo de ordenação rápida.

VAntagens

.Muito rápido na maioria dos casos (O(n log n)).
.Usa pouca memória, já que é implementado de forma recursiva.

Desvantagens

.Pode ter desempenho ruim no pior caso (O(n²)), se p pivô for mal escolhido.
.Não é estável (pode mudar a ordem de elementos iguais).
'''