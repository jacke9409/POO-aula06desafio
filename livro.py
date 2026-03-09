from item_biblioteca import ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__ (self, codigo, titulo, ano, disponivel, autor, num_paginas):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", autor: {self.__autor}, num_paginas: {self.__num_paginas}"
