from item_biblioteca import ItemBiblioteca

class DVD(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, diretor, duracao):
        super().__init__(codigo, titulo, ano)
        self.__diretor = diretor
        self.__duracao = duracao

    def exibir_detalhes(self):
        print(f"[DVD] ", end="")
        super().exibir_detalhes()
        print(f"Diretor: {self.__diretor} | Duração: {self.__duracao} min")