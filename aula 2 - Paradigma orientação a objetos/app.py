# 3 importar o arquivo que contém a classe Restaurante
from modelos.restaurante4 import Restaurante

# 4 criar um objeto(instância de Restaurante)
restaurante_praca=Restaurante('praça','gourmet')
restaurante_mexicano=Restaurante('mexican food','mexicana')
restaurante_japones=Restaurante('japa','japonesa')


# alternar estado de um restaurante
restaurante_japones.alternar_estado()


# criando avaliações para o restaurante praça
restaurante_praca.receber_avaliacao('Barbado',8)
restaurante_praca.receber_avaliacao('Tigogo',5.5)

restaurante_mexicano.receber_avaliacao('Palermo',10)
restaurante_mexicano.receber_avaliacao('Hobson',7)

restaurante_japones.receber_avaliacao('Galego',5)
restaurante_japones.receber_avaliacao('Boris',8)

# 2 criando a chamada da função de entrada
def main():
    # 5 inserir uma ação dentro do main
    Restaurante.listar_restaurantes()
    

if __name__=='__main__':
    main()