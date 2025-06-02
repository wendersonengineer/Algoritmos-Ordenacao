
# SELECTION SORT

def selection_sort(lista):
     tamanho_lista = len(lista)
     for indice_atual in range(tamanho_lista - 1):
        indice_menor = indice_atual
        for i in range(indice_atual +  1,  tamanho_lista):
            if lista[i] < lista[indice_menor]:
                indice_menor = i
            if indice_menor != indice_atual:
                lista[indice_atual], lista[indice_menor] = lista[indice_menor], lista[indice_atual]

numeros = [10, 2, 4, 5, 1, 3, 20, 87, 52, 54,  15]
selection_sort(numeros)
print("Lista ordenada")
print(numeros)

'''Selecion sort - Algoritimo de ordenação por seleção

Vantagens

. A vantagem da ordenação por seleção é sua simplicidade e requisitos mínimos de memória.
. É fácil de entender e implementar, o que a torna uma boa opção para ensino de conceitos 
básicosde ordennação.

Desvantagens

. A complexidade temporal da ordenação por seleção de O(n²) significa que, 
à  medidade que o número de elementos  no conjunto de dados aumenta,
o tempo necessário para ordenação aumenta drasticamente. 
Isso a torna impraticável para matrizes ou listas grandes.'''