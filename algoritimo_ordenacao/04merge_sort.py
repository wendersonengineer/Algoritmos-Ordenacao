
# MERGE SORT

def merge_sort(lista):

    if len(lista) > 1:
        meio_lista = len(lista) // 2

        parte_esquerda = lista[:meio_lista]

        parte_direita = lista[meio_lista:]

        merge_sort(parte_esquerda)
        merge_sort(parte_direita)

        indice_esquerda = indice_direita = indice_lista = 0

        # Mescla as duas metades ordenadas

        while indice_esquerda < len(parte_esquerda) and indice_direita < len(parte_direita):
            if parte_esquerda[indice_esquerda] < parte_direita[indice_direita]:
                lista[indice_lista] = parte_esquerda[indice_esquerda]
                indice_esquerda += 1
            else:
                lista[indice_lista] = parte_direita[indice_direita]
                indice_direita += 1
            indice_lista += 1

        # Adiciona elementos restantes da parte esquerda, se houver

        while indice_esquerda < len(parte_esquerda):
            lista[indice_lista] = parte_esquerda[indice_esquerda]
            indice_esquerda += 1
            indice_lista += 1

        # Adiciona elementos restantyes da parte direita, se houver

        while indice_direita < len(parte_direita):
            lista[indice_lista] = parte_direita[indice_direita]
            indice_direita += 1
            indice_lista += 1

numeros_desordenados = [64, 43, 25, 12, 22, 12, 11, 64, 90]

merge_sort(numeros_desordenados)

print(numeros_desordenados)

'''Merge Sort

Vantagens
.Complexidade 0(n log n), eficiente para grandes lista.
.Algoritmo estável (mantém a ordem de elementos iguais) '''