# 2) Classe de controle (obrigatória)
# Biblioteca
# Atributos:
# • __itens (lista)
# Métodos:
# • adicionar_item(item) → aceita Livro ou Revista
# (lista de itens)
# • listar_itens() → chama exibir_detalhes() de
# cada item (polimorfismo acontecendo aqui)
# • buscar_por_codigo(codigo)
# • emprestar_item(codigo)
# • devolver_item(codigo)

class Biblioteca:
    def __init__(self):
        self.__itens = []

    def adicionar_item(self, item):
        # Aceita Livro ou Revista (idealmente classes filhas de uma classe base comum)
        self.__itens.append(item)

    def listar_itens(self):
        if not self.__itens:
            print("A biblioteca está vazia.")
            return
        
        for item in self.__itens:
            # Polimorfismo: cada objeto chama sua própria versão de exibir_detalhes()
            item.exibir_detalhes()
            print("-" * 20)

    def buscar_por_codigo(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo: # Assume que o objeto possui o atributo 'codigo'
                return item
        return None

    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            return item.emprestar() # Assume que o item tem o método 'emprestar'
        print("Item não encontrado.")
        return False

    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            return item.devolver() # Assume que o item tem o método 'devolver'
        print("Item não encontrado.")
        return False