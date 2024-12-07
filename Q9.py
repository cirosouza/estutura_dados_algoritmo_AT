import time
import random
import string

class TabelaHash:
    def __init__(self, tamanho):
        # gera um objeto com um parametro de tamanho e uma lista de listas com "tamanho" listas dentro de outra lista
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        # Gear um indice que fica entre 0 e (self.tamanho - 1)
        # Garante uma distribuição uniforme dos elementos nos diferentes indices permitidos
        return hash(chave) % self.tamanho
    
    def inserir(self, nome_usuario, perfil):

        indice = self._hash(nome_usuario)
        # Busca a chave e caso ja exista, atualiza o valor
        for item in self.tabela[indice]:
            if item[0] == nome_usuario:
                item[1] = perfil
        
        # Caso a chave nao exista, cria um novo par chave valor
        self.tabela[indice].append([nome_usuario,perfil])


    def buscar(self, nome_usuario):

        indice = self._hash(nome_usuario)
        # retorna o valor para a chave dada caso exista
        for item in self.tabela[indice]:
            if item[0] == nome_usuario:
                return item[1]
        # retorna None caso não exista chave
        return None

    def remover(self, nome_usuario):

        indice = self._hash(nome_usuario)
        # remove o item caso a chave , retorna True caso exista sucesso na remoção
        for item in self.tabela[indice]:
            if item[0] == nome_usuario:
                self.tabela[indice].remove(item)
                return True
        
        # retorna False caso não exista a chave informada
        return False



# Função para medir o tempo de busca
def medir_tempo_busca(funcao_busca, entrada, nome_usuario):
    inicio = time.time()
    resultado = funcao_busca(entrada, nome_usuario)
    fim = time.time()
    tempo_execucao = fim - inicio
    return resultado, f"Tempo de execução: {tempo_execucao:.10f} segundos."

# Função de busca na lista linear
def busca_linear(lista, nome_usuario):
    for nome, perfil in lista:
        if nome == nome_usuario:
            return perfil
    return None

# Função para gerar strings aleatórias (nomes de usuários)
def gerar_string_aleatoria(tamanho=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

# Função para gerar uma coleção aleatória de usuários
def gerar_usuarios_aleatorios(quantidade):
    usuarios = []
    for _ in range(quantidade):
        nome_usuario = gerar_string_aleatoria()
        perfil = {
            "nome": gerar_string_aleatoria(5),
            "idade": random.randint(18, 60),
            "cidade": gerar_string_aleatoria(10)
        }
        usuarios.append((nome_usuario, perfil))
    return usuarios

# Gerar coleção com milhares de usuários
quantidade_usuarios = 100000  # Ajuste este valor para testar diferentes volumes
usuarios_aleatorios = gerar_usuarios_aleatorios(quantidade_usuarios)

# Criar TabelaHash e lista linear
tabela_hash = TabelaHash(tamanho=200000)
lista_linear = []

# Inserir os usuários na TabelaHash e na lista linear
for nome_usuario, perfil in usuarios_aleatorios:
    tabela_hash.inserir(nome_usuario, perfil)
    lista_linear.append((nome_usuario, perfil))


# Selecionar um usuário aleatório para busca
nome_usuario_busca = random.choice(usuarios_aleatorios)[0]


# Testando a busca na TabelaHash
resultado_hash, tempo_hash = medir_tempo_busca(lambda t, n: t.buscar(n), tabela_hash, nome_usuario_busca)
print(f"Resultado na TabelaHash: {resultado_hash}")
print(tempo_hash)

# Testando a busca na lista linear
resultado_linear, tempo_linear = medir_tempo_busca(busca_linear, lista_linear, nome_usuario_busca)
print(f"Resultado na busca linear: {resultado_linear}")
print(tempo_linear)

