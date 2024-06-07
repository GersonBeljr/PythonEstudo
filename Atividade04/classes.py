class Livro:
    biblioteca = []
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        
        Livro.biblioteca.append(self)
        
    def __str__(self):
        return f'Titulo: {self.titulo};\nAutor: {self.autor};\nAno da publicação: {self.ano_publicacao}.'
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'Livro {self.titulo} emprestado com sucesso')
        else:
            print(f'Livro {self.titulo} não disponivel para emprestimo')
        
        
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_ano = []
        
        for livro in Livro.biblioteca:
            if livro.ano_publicacao == ano:
                if livro.disponivel:  
                    livros_ano.append(livro.titulo)
        
        print(f'Os livros disponiveis de {ano} são: ')
        
        for livro in livros_ano:
            print(f' - {livro}')
            