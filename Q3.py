def busca_contato(nome, lista_contatos):
    # Realiza a iteração na lista de contatos ate encontrar o nome igual ao parametro
    # Parametro lista_contatos é um conjunto de tuplas com nome e telefone dos contatos
    for contato in lista_contatos:
        if contato[0] == nome:
            return f"O telefone de {contato[0]} é {contato[1]}."
        
    # Retorna none caso o nome nao tenha sido encontrado
    return "Não existe contato com esse nome."

lista_contatos_exemplo = {
    ("João", "1234-5678"),
    ("Maria", "2345-6789"),
    ("Carlos", "3456-7890"),
    ("Ana", "4567-8901"),
    ("Lucas", "5678-9012")
}

print(busca_contato("Lucas", lista_contatos_exemplo))
print(busca_contato("Ana", lista_contatos_exemplo))
print(busca_contato("Chico", lista_contatos_exemplo))

