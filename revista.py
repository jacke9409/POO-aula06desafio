from item_biblioteca import ItemBiblioteca
class revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, disponivel,edicao, mes):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__edicao = edicao 
        self.__mes = mes

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", edicao: {self.__edicao}, mes: {self.__mes}"