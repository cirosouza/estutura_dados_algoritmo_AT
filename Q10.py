class Navegador:
    # Simula o comportamento de um navegador
    # Registra o caminho dos acessos atraves do uso de uma pilha principal e uma pilha auxiliar

    def __init__(self):
        self.pilha_atual = []
        self.pilha_avancar = []

    def visitar_pagina(self, url):

        # Adiciona a nova pagina a pilha atual
        if self.pilha_atual:
            print(f"Saiu da página: {self.pilha_atual[-1]}")
        self.pilha_atual.append(url)
        
        # Limpa a pilha auxiliar porque uma nova pagina foi acessada e o caminho foi alterado
        self.pilha_avancar = []
        print(f"Visitando página: {url}")

    def voltar(self):
        # retorna para a pagina anterior acessando o ultimo item da pilha atual
        if len(self.pilha_atual) > 1:
            url_atual = self.pilha_atual.pop()  # Remove a página atual

            # Adiciona à pilha de avanço a pilha atual, formando o caminho dos acessos
            self.pilha_avancar.append(url_atual)
            print(f"Voltando para: {self.pilha_atual[-1]}")
        else:
            print("Não é possível voltar, já está na primeira página.")
    
    def avancar(self):
        # avanca para a proxima pagina
        # remove pagina da lista auxiliar de avanço e adiciona a lista principal
        if self.pilha_avancar:
            url = self.pilha_avancar.pop()  
            self.pilha_atual.append(url)  
            print(f"Avançando para: {url}")
        else:
            print("Não há páginas para avançar.")

    def mostrar_status(self):
        # Exibe situação atual das pilhas
        print("\nStatus atual:")
        print(f"Pilha Atual: {self.pilha_atual}")
        print(f"Pilha Avançar: {self.pilha_avancar}")
        print()


# Simulação do sistema de navegação
navegador = Navegador()

# Visitando páginas
navegador.visitar_pagina("www.google.com")
navegador.visitar_pagina("https://lms.infnet.edu.br/moodle/login/index.php")
navegador.visitar_pagina("www.github.com")

# Voltando para páginas anteriores
navegador.voltar()
navegador.voltar()

# Avançando para páginas seguintes
navegador.avancar()

# Visitando uma nova página (limpa a pilha de avanço)
navegador.visitar_pagina("www.wikipedia.org")

# Voltando para páginas anteriores
navegador.voltar()

# Mostrando status final
navegador.mostrar_status()

    
