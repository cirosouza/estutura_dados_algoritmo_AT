class No:
    # Classe que representa um nó da árvore
    # O nó possui uma chave que representa  codigo dos produtos
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
        
    def _navega_esquerda(self, no_atual):
        # Navega para os nós a esquerda procurando o nó limite com o menor valor
        if no_atual.esquerda is None:
            return no_atual
        else:
            return self._navega_esquerda(no_atual.esquerda)
    
    def encontra_menor(self, no_atual):
        # Retorna o no com a menor chave após busca recursiva
        return self._navega_esquerda(no_atual)

    def remover(self, chave):
        # Chama a função interna de remoção
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no_atual, chave):
        # Testa se o nó atual é vazio e retorna sem executar operações
        if no_atual is None:
            return no_atual
        
        # Navegar para esquerda ou direita para remoção, a depender do valor da chave
        if chave < no_atual.chave:
            no_atual.esquerda = self._remover(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._remover(no_atual.direita, chave)
        else:
            # Caso do nó folha, sem filhos
            # A busca termina sem resultado, retorna None
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
            # Caso do nó com um filho, retorna o no existente para ocupar o espaço do no removido
            elif no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            # Caso do nó com dois filhos
            # Busca o menor nó do ramo da direita e posiciona no lugar do no removido
            # Reposiciona os demais nós
            else:
                sucessor = self.encontra_menor(no_atual.direita)
                no_atual.chave = sucessor.chave
                no_atual.direita = self._remover(no_atual.direita, sucessor.chave)

        # Retorna o no atual após as operações
        return no_atual
    
    def ordem_crescente_elementos(self):
        elementos = []
        # Chama a função interna recursiva de ordenação em lista dos elementos
        self._ordem_crescente_elementos(self.raiz, elementos)
        return elementos

    def _ordem_crescente_elementos(self, no_atual, elementos):
        # navega pelos elementos da esquerda e posiciona-os na lista a partir do menor encontrado
        if no_atual is not None:
            self._ordem_crescente_elementos(no_atual.esquerda, elementos)
            elementos.append(no_atual.chave)
            self._ordem_crescente_elementos(no_atual.direita, elementos)

# Instanciar a árvore e inserir os códigos
arvore_produtos = ArvoreBuscaBinaria()
codigos = [45, 25, 65, 20, 30, 60, 70]
for codigo in codigos:
    arvore_produtos.inserir(codigo)

# Função para exibir a árvore em ordem crescente
def exibir_arvore(arvore):
    print("Árvore em ordem crescente:", arvore.ordem_crescente_elementos())

# Exibir a árvore inicial
print("Árvore inicial:")
exibir_arvore(arvore_produtos)

# Remover o nó folha (20)
print("\nRemovendo o nó folha (20):")
arvore_produtos.remover(20)
exibir_arvore(arvore_produtos)

# Remover o nó com um filho (25)
print("\nRemovendo o nó com um filho (25):")
arvore_produtos.remover(25)
exibir_arvore(arvore_produtos)

# Remover o nó com dois filhos (45)
print("\nRemovendo o nó com dois filhos (45):")
arvore_produtos.remover(45)
exibir_arvore(arvore_produtos)


