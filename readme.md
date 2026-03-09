------------------------------------
descrição projeto: Sistema de Gestão de Biblioteca (POO +
GitHub)
------------------------------------

-----------------------------------------------------------------------------
Criar um sistema simples de gestão de itens de uma biblioteca, com cadastro, 
empréstimos e devolução.
------------------------------------------------------------------------------

-----------------------------------------------------------------------------
Objetivos
usar encapsulamento,herança, polimorfismo, organização e Git/Github
-----------------------------------------------------------------------------

----------------------------------------------------------------------------
1. Cadastrar livro
1. Cadastrar Revista
3.Listar Itens
4.Emprestar Item(Por código)
5.Devolver item(por código)

 Conceitos de POO Aplicados
*   **Abstração**: Criação de modelos para itens reais da biblioteca.
*   **Encapsulamento**: Uso de atributos privados (`__atributo`) e decoradores `@property` para getters e setters com validações.
*   **Herança**: As classes `Livro` e `Revista` herdam atributos e métodos da superclasse `ItemBiblioteca`.
*   **Polimorfismo**: O método `exibir_detalhes()` é sobrescrito nas subclasses para exibir informações específicas de cada tipo de item.
-------------------------------------------------------------
* **no bonus, foi criado uma subclasse extra chamada dvd.py**
-------------------------------------------------------------

nela vai estar os itens emprestados e os disponiveis