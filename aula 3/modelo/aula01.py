# Herança de classe
class Programa:
    catalago = []
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

        Programa.catalago.append(self)
    
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes +=1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        
class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self._temporadas = temporadas

filme1 = Filme('star wars', 1977, 132)
filme1.dar_likes()
print(f'{filme1.nome} {filme1.ano} {filme1.duracao} {filme1._likes}')

serie1 = Serie('Grays anatomy',2005,20)
while serie1._likes <= 9999:
    serie1.dar_likes()
print(f'{serie1.nome} {serie1.ano} {serie1._temporadas} {serie1._likes}')
