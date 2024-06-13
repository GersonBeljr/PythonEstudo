# polimorfismo
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
        
    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.likes} likes')
        
class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
    
    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes')
        
class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    
    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.temporadas} temps - {self.likes} likes')
        

filme1 = Filme('star wars', 1977, 132)
filme1.dar_likes()
# print(f'{filme1.nome} {filme1.ano} {filme1.duracao} {filme1._likes}')

serie1 = Serie('Grays anatomy',2005,20)
while filme1._likes <= 9999:
    serie1.dar_likes()
    filme1.dar_likes()
# print(f'{serie1.nome} {serie1.ano} {serie1._temporadas} {serie1._likes}')


for programacao in Programa.catalago:
    Programa.imprime(programacao)
