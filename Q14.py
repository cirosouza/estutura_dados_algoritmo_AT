class No:
    # Classe que representa um nó da árvore
    # O nó possui uma chave que no exemplo será o preço do produto
    # A arvore é ordenada de forma que o no esquerdo possui chave menor que o pai e o diretio, maior
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    # Classe para construção da arvore de busca binaria
    def __init__(self):
        self.raiz = None

    # Método público de inserção de novos elementos na árvore
    def inserir(self, chave):
        # Verifica se a raiz da arvore ja possui chave e adiciona caso e caso negativo
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            # Chama o metodo interno de inserção para buscar o nó correto para inserir a chave
            self._inserir(self.raiz, chave)

    def _inserir(self, no_atual, chave):
        # Metodo interno de inserção
        # Verifica se o valor da chave é menor que a chave do no atual
        if chave < no_atual.chave:
            # Verifica se o no atual ja tem chave e associa caso negativo
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave)
            # Desce um nível da árvore caso o nó ja tenha chave
            else:
                self._inserir(no_atual.esquerda, chave)
        # Verifica se a chave é maior que a chave do no atual
        elif chave > no_atual.chave:
            # Vrifica se o no possui chave, caso nagativo, associa a chave
            if no_atual.direita is None:
                no_atual.direita = No(chave)
            # Desce um nível na árvore caso o nó já possua chave
            else:
                self._inserir(no_atual.direita, chave)

    def buscar(self, chave):
        # Método publico de busca por chaves
        # Chama o método interno de busca e inicia pelo no raiz
        return self._buscar(self.raiz, chave)
    
    def _buscar(self, no_atual, chave):
        # Metodo interno de busca
        # Verifica se existe o no atual e retorna Falso caso nao exista
        if no_atual is None:
            return False
        # Verifica se a chave em busca é a chave do no atual
        if no_atual.chave == chave:
            return True
        # Verifica se a chave em busca é menor ou maior que a chave do no atual
        elif chave < no_atual.chave:
            # Chamada recursiva no metodo de busca para o no esquerdo caso a chave seja menor que a do no pai
            return self._buscar(no_atual.esquerda, chave)
        else:
            # Chamada recursiva no metodo de busca para o no direito caso a chave seja maior que a do no pai
            return self._buscar(no_atual.direita, chave)
        

# Exemplo de aplicação da árvore
arvore_exemplo = ArvoreBuscaBinaria()

# Inserir os preços na arvore binaria de busca
precos = [100, 50, 150, 30, 70, 130, 170]
for preco in precos:
    arvore_exemplo.inserir(preco)

# Verificar se o preço 70 está disponível
preco_a_buscar = 70

resultado = arvore_exemplo.buscar(preco_a_buscar)
if resultado:
    print(f"Preço {preco_a_buscar} está disponível na loja.")
else:
    print(f"Preço {preco_a_buscar} não foi encontrado.")