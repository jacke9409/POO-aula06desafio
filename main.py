# Sistema de gestão de Biblioteca (POO + GitHub)

#  Criar um sistema de gestão de itens de uma biblioteca, com cadastro, empréstimo e devolução
# Regras do sistema( requisitos)
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
class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel
