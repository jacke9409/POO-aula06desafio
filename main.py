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

        op = input("Escolha uma opção: ")

        if op == "1":
            bib.adicionar_item(Livro(input("Cód: "), input("Título: "), int(input("Ano: ")), input("Autor: "), input("Páginas: ")))
        elif op == "2":
            bib.adicionar_item(Revista(input("Cód: "), input("Título: "), int(input("Ano: ")), input("Edição: "), input("Mês: ")))
        elif op == "3":
            bib.adicionar_item(DVD(input("Cód: "), input("Título: "), int(input("Ano: ")), input("Diretor: "), input("Duração(min): ")))
        elif op == "4":
            bib.listar_itens()
        elif op == "5":
            bib.emprestar_item(input("Código: "))
        elif op == "6":
            bib.devolver_item(input("Código: "))
        elif op == "7":
            bib.gerar_relatorio_status(disponivel=True)
        elif op == "8":
            bib.gerar_relatorio_status(disponivel=False)
        elif op == "9":
            break

if __name__ == "__main__":
    menu()