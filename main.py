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