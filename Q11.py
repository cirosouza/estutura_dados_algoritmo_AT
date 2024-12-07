class SistemaAtendimento:
    def __init__(self):
        # A fila inicia sem chamados e é repersentada por uma lista
        self.fila_atendimento = []

    def inserir_chamado(self, chamado):
        # Insere o chamado no final da fila
        self.fila_atendimento.append(chamado)
        print(f"Novo chamado inserido na fila => {chamado}")
    
    def atender_chamado(self):
        # O chamado que chegou primeiro é atendido primeiro
        # A regra FIFO da fila é obedecida
        chamado_atendimento = self.fila_atendimento.pop(0)
        print(f"O chamado está em atendimento => {chamado_atendimento}")

    def exibir_fila(self):
        if self.fila_atendimento:
            print("\n----- FILA DE ATENDIMENTO -----")
            for chamado in self.fila_atendimento:
                print(f"O {self.fila_atendimento.index(chamado) + 1}º da fila de atendimento é: {chamado}")
        else:
            print("\n----- A FILA ESTÁ VAZIA -----")


# Inicializando o sistema de atendimento
sistema = SistemaAtendimento()

# Adicionando chamados à fila
sistema.inserir_chamado("Maria Silva: Problema com pagamento")
sistema.inserir_chamado("João Oliveira: Dúvida sobre produto")
sistema.inserir_chamado("Ana Costa: Reembolso não processado")
sistema.inserir_chamado("Carlos Almeida: Erro no login")
sistema.inserir_chamado("Luciana Pereira: Atualização de cadastro")

# Exibindo a fila inicial
sistema.exibir_fila()

# Atendendo dois chamados
print("\n--- Atendendo chamados ---")
sistema.atender_chamado()  # Maria Silva
sistema.atender_chamado()  # João Oliveira

# Exibindo a fila após os atendimentos
sistema.exibir_fila()

# Adicionando mais chamados
print("\n--- Inserindo novos chamados ---")
sistema.inserir_chamado("Fernanda Lima: Problema com a entrega")
sistema.inserir_chamado("Ricardo Santos: Consulta de saldo")

# Exibindo a fila final
sistema.exibir_fila()

