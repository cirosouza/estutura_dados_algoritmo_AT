def knapsack_solver(pesos, valores, capacidade):
    # Soluciona o problema da mochila usando programação dinâmica
    # Retorna o melhor valor possível e os itens selecionados na melhor solução

    n = len(pesos)
    
    # Criação da tabela dp
    # As linhas das tabelas representam os itens em ordem crescente de peso
    # As colunas representam mochilas com capacidade 0 ate a capacidade maxima da mochila do problema
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenchendo a tabela dp
    # Iteração sobre as linhas
    for i in range(1, n + 1):
        # Iteração sobre as colunas
        for w in range(1, capacidade + 1):
            # Verifica se o peso do item atual é menor ou igual a capacidade
            if pesos[i - 1] <= w:
                # Aqui é onde se decide sobre a inclusão do item atual
                # Há uma avaliação se é melhor só repetir o melhor valor anterior
                #   ou incluir o item atual e somar isso ao melhor resultado possível com a capacidade restante
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                # Se o item atual nao pode ser escolhido, associa-se o valor da melhor solução anterior
                dp[i][w] = dp[i - 1][w]
    
    # O valor maximo possível é encontrado no canto inferior direito da tabela
    valor_maximo = dp[n][w]

    # Rastreando os itens selecionados
    itens_selecionados = []
    # Inicia a busca pela coluna de maior capacidade
    w = capacidade
    for i in range(n, 0, -1):
        # Percorre as linhas de baixo para cima
        # Se o valor da celula atual é diferente do valor da celula acima, é porque o item foi incluido na melhor solucao
        if dp[i][w] != dp[i - 1][w]:
            # Adiciona o índice do item a lista de selecionados
            itens_selecionados.append(i - 1) 
            # Reduz a capacidade considerando que o item ja foi selecionado
            w -= pesos[i - 1]  

    # Reverte a lista para exibir os itens na ordem original
    itens_selecionados.reverse()

    return valor_maximo, itens_selecionados

# Exemplo de teste
pesos_exemplo = [1, 3, 4, 5]
valores_exemplo = [10, 40, 50, 70]
capacidade_exemplo = 8

valor_maximo, itens_selecionados = knapsack_solver(pesos_exemplo, valores_exemplo, capacidade_exemplo)
print(f"Valor máximo que pode ser obtido: {valor_maximo}")
print(f"Itens selecionados (índices): {itens_selecionados}")
print(f"Itens selecionados (pesos): {[pesos_exemplo[i] for i in itens_selecionados]}")
print(f"Itens selecionados (valores): {[pesos_exemplo[i] for i in itens_selecionados]}")
