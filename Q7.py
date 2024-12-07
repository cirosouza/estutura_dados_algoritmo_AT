class TabelaHash:
    def __init__(self, tamanho):
        # gera um objeto com um parametro de tamanho e uma lista de listas com "tamanho" listas dentro de outra lista
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        # Gear um indice que fica entre 0 e (self.tamanho - 1)
        # Garante uma distribuição uniforme dos elementos nos diferentes indices permitidos
        return hash(chave) % self.tamanho
    
    def inserir(self, valor):

        indice = self._hash(valor)
        if valor not in self.tabela[indice]:
            self.tabela[indice].append(valor)

    def contem(self, valor):
        indice = self._hash(valor)
        return valor in self.tabela[indice]
    
# Função para verificar duplicidades usando a classe TabelaHash
def possui_duplicidade(lista):
    hashtable = TabelaHash(len(lista))  # Cria uma instância de TabelaHash
    for item in lista:
        if hashtable.contem(item):
            return True
        hashtable.inserir(item)
    return False

# Testando a solução
lista_ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 2]
lista_ex2 = [5,7,21,6,9,55,4,65,26]

result = possui_duplicidade(lista_ex1)
print("Há duplicidade em lista_ex1?", result)
result = possui_duplicidade(lista_ex2)
print("Há duplicidade em lista_ex2?", result)

