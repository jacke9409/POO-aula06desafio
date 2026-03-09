# Sistema de gestão de Biblioteca (POO + GitHub)

#  Criar um sistema de gestão de itens de uma biblioteca, com cadastro, empréstimo e devolução
# Regras do sistema( requisitos)
from biblioteca import Biblioteca
from livro import Livro
from revista import Revista

def adicionar_item(self, novo_item):
    # Validação de código único (Bônus)
    if self.buscar_por_codigo(novo_item.codigo):
        print(f"Erro: Código {novo_item.codigo} já existe!")
    else:
        self.__itens.append(novo_item)

def menu():
    bib = Biblioteca()
    while True:
        print("\n--- SISTEMA DE BIBLIOTECA (MODO BÔNUS) ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Revista")
        print("3. Cadastrar DVD") # Bônus
        print("4. Listar Itens")
        print("5. Emprestar Item")
        print("6. Devolver Item")
        print("7. Relatório: Disponíveis") # Bônus
        print("8. Relatório: Emprestados") # Bônus
        print("9. Sair")