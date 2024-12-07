def selection_sort(ranking_jogadores):
    # O parametro é uma lista com os dados dos jogadores organizados em dicionarios
    # A ordenação é realizada em ordem decrescente
    # A função altera a propria coleção que foi inserida como parametro
    # registra o tamanho da coleção em uma variavel
    n = len(ranking_jogadores)
    for i in range(n):
        # A variavel indice_maior guarda o indice do maior valor, ela é iniciada com o indice atual do loop
        indice_maior = i
        # itera sobre os outros itens da lista e compara com o valor do item atual
        # caso algum item tenha valor maior, o indice é associado a variavel indice_maior
        for j in  range(i + 1, n):
            if ranking_jogadores[j]["Pontuação"] > ranking_jogadores[indice_maior]["Pontuação"]:
                indice_maior = j

        # É realizada a troca de posições entre a variável atual do loop e o maior valor encontrado na parte desordenada da coleção
        ranking_jogadores[i], ranking_jogadores[indice_maior] = ranking_jogadores[indice_maior], ranking_jogadores[i]


# Exemplo de uso
jogadores = [
    {"Nome": "Alice", "Pontuação": 1200},
    {"Nome": "Bob", "Pontuação": 800},
    {"Nome": "Charlie", "Pontuação": 1500},
    {"Nome": "Diana", "Pontuação": 950},
    {"Nome": "Eve", "Pontuação": 1350},
    {"Nome": "Frank", "Pontuação": 700},
    {"Nome": "Grace", "Pontuação": 1450},
    {"Nome": "Hank", "Pontuação": 1100},
    {"Nome": "Ivy", "Pontuação": 900},
    {"Nome": "Jack", "Pontuação": 1250},
]


selection_sort(jogadores)

# Imprimindo os jogadores ordenados
for jogador in jogadores:
    print(f"{jogador['Nome']} - {jogador['Pontuação']} pontos")



