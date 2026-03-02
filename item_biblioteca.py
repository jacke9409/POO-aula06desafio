# 1) Classes obrigatórias
# ItemBiblioteca(superclasse)
# Você foi contratado para criar um sistema simples de
# gestão de itens de uma biblioteca, com cadastro,
# empréstimo e devolução. A biblioteca possui diferentes
# tipos de itens (ex.: livros e revistas), e cada tipo tem regras
# próprias.
# Atributos(encapsulados): 
# Métodos obrigatórios:
# • exibir_detalhes() → polimórfico (vai existir nas
# subclasses)
# • emprestar() → muda __disponivel para False se
# estiver disponível
# • devolver() → muda __disponivel para True
# • getters e setters com validações simples (ex.: ano > 0,
# título não vazio)
# Obrigatório: todas as saídas devem usar print com f-
# strings.


class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        return f"codigo: {self.__codigo}, titulo: {self.__titulo}, ano: {self.__ano}, disponivel: {self.__disponivel}"

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Item {self.__titulo} emprestado com sucesso.")
        else:
            print(f"Item {self.__titulo} não está disponível para empréstimo.")
    
    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"Item {self.__titulo} devolvido com sucesso.")
        else:
            print(f"Item {self.__titulo} já está disponível na biblioteca.")

    # Getters e Setters

#     Livro (subclasse de ItemBiblioteca)
# Atributos extras (encapsulados):
# • __autor
# • __num_paginas
# Regras:
# • Sobrescreva exibir_detalhes() mostrando que é
# um Livro e exibindo autor + páginas.
# Revista (subclasse de ItemBiblioteca)
# Atributos extras (encapsulados):
# • __autor
# • __num_paginas

class livro(ItemBiblioteca):
    def __init__ (self, codigo, titulo, ano, disponivel, autor, num_paginas):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", autor: {self.__autor}, num_paginas: {self.__num_paginas}"
