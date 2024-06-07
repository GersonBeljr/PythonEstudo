from classes import Livro

livroTest1 = Livro('Donquixote','Miguel de Cervantes','1605')
livroTest2 = Livro('Ozob','Daive Pazos','2018')
livroTest3 = Livro('Biblia','Deus?','0')
livroTest4 = Livro('Parangas','Tonin','2018')
livroTest5 = Livro('Rogisrogis','Rogis','1605')
livroTest6 = Livro('Tabacudo','Cleitom','2018')
livroTest7 = Livro('A arte Hoje','Paive Dazos','1605')
livroTest8 = Livro('A arte de guerra em quadrinhos','Samuel','2018')
livroTest9 = Livro('O segredo','Segredo','1605')


livroTest1.emprestar()
livroTest2.emprestar()

Livro.verificar_disponibilidade('2018')

def main():
    pass

if __name__=='__main__':
    main()