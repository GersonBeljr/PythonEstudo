print('')
# 1 criar uma classe Restaurante usando contrutor

class Restaurante:
    restaurantes=[]

    def __init__(this,nome,categoria):
        this.nome = nome
        this.categoria = categoria
        this.ativo = False
        
        Restaurante.restaurantes.append(this)

    def __str__(this):
        return f'{this.nome.ljust(15)} | {this.categoria}'
    
    # metodo de listagem de restaurantes
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(15)} | {restaurante.categoria.ljust(15)} | {restaurante.ativo}')

# 2 criação de objetos

rest_praca = Restaurante('praça','Gourmet')
rest_pizza = Restaurante('Pizza Express','Turco')

# 3 consumindo os objetos


print(vars(rest_praca))
print(vars(rest_pizza))
print('')

print((rest_praca))
print((rest_pizza))
print('')

# consumindo listar restaurantes

Restaurante.listar_restaurantes()