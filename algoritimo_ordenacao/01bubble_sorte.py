
# BUBBLE SORT

def bublle_sort (lista):

    tamanho_lista = len(lista)
    
    for posicao_atual in range(tamanho_lista-1):

        for i in range(tamanho_lista-1):   

            if lista[i] > lista[i+1]:

                lista[i], lista[i+1] =  lista[i+1], lista[i]

numeros = [64, 43, 25, 12, 22, 11, 90]
bublle_sort(numeros)
print("Lista Ordenada")
print(numeros)


'''BUBBLE SORT - Algoritmo de ordenação por bolha.

Vantagens

. Fácil de implementar e compreender.
. Bom para listas pequenass.

Desvantagens

. Complexidade 0(n²),  tornado-o ineficiente para grandes volumes de dados.
. Muitas trocas, o que o tornando ineficiente para listas longas.
''' 

    

