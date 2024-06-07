# 1 criar um decorator @property
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    # 4 criar método para listar os restaurantes
    # método de classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'

    # método de objeto
    def alternar_estado(self):
        self._ativo=not self._ativo

# 2 criação de objetos
restaurante_praca=Restaurante('praça','Gourmet')
restaurante_praca._nome='biqueira'
restaurante_praca.alternar_estado()

restaurante_pizza=Restaurante('pizza express','Italiana')




# 3 consumindo os objetos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')

# print(restaurante_praca)
# print(restaurante_pizza)
# print('')

# 5 consumindo o método listar_restaurantes
Restaurante.listar_restaurantes()


