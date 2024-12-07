import random
import time

def bubble_sort(lista_precos):
    tamanho = len(lista_precos)

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista_precos[j] > lista_precos[j + 1]:
                lista_precos[j], lista_precos[j + 1] = lista_precos[j + 1], lista_precos[j]


def medir_tempo_ordenacao(dados):
    inicio = time.time()
    bubble_sort(dados)
    fim = time.time()
    tempo_de_execucao = fim - inicio
    return f"O tempo de execução para ordenar {len(dados)} elementos foi de {tempo_de_execucao:.6f} segundos."

lista_1000 = [random.uniform(0, 500) for _ in range(1000)]
lista_10000 = [random.uniform(0, 500) for _ in range(10000)]


print(medir_tempo_ordenacao(lista_1000))
print(medir_tempo_ordenacao(lista_10000))
