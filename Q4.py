import random

def busca_binaria(dados, isbn_buscado):
    menor_indice, maior_indice = 0, len(dados) - 1
    iteracoes = 0

    while menor_indice <= maior_indice:
        iteracoes += 1

        indice_meio = (menor_indice + maior_indice) // 2

        if dados[indice_meio] == isbn_buscado:
            return indice_meio, iteracoes
        elif dados[indice_meio] < isbn_buscado:
            menor_indice = indice_meio + 1
        else:
            maior_indice = indice_meio - 1
        
    return "ISBN nao encontrado.", iteracoes

def busca_linear(dados, isbn_buscado):
    iteracoes = 0

    for i, valor in enumerate(dados):
        iteracoes += 1
        if valor == isbn_buscado:
            return i, iteracoes
    
    return "ISBN nao encontrado.", iteracoes

lista_de_isbns = sorted(random.randint(1000000000000, 9999999999999) for _ in range(100000))



# Exibição do resultado
for i in range(1,5):
    print(f"------ {i}º TESTE  ------")
    # Escolha de um ISBN aleatório para busca
    isbn_alvo = random.choice(lista_de_isbns)

    # Execução da busca com os dois tipos de algoritmo
    resultado_binario, iteracoes_binario = busca_binaria(lista_de_isbns, isbn_alvo)
    resultado_linear, iteracoes_linear = busca_linear(lista_de_isbns, isbn_alvo)
    print(f"O resultado para busca binaria foi: {resultado_binario} em {iteracoes_binario} iterações.")
    print(f"O resultado para busca linear foi: {resultado_linear} em {iteracoes_linear} iterações.")


