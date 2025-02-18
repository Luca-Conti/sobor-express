from colorama import Fore
class Restaurante():
    restaurantes = []
    def __init__(self, nome, categoria):  
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avalicao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} || {'Categoria do Restaurante'.ljust(25)} || {'Avaliação'.ljust(25)} || Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} || {restaurante._categoria.ljust(25)} || {str(restaurante.medeia_avaliacao).ljust(25)} || {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_status(self):
        self._ativo = not self._ativo