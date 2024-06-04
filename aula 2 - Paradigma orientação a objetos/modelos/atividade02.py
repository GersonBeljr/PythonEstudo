def funcaolegal(quest,texto):
    print('')
    print(f'Questão: {quest}')
    print(vars(texto))
    print('')

# Questão 1
class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Palio El','Prata',"1996")
funcaolegal('1',carro1)

# Questão 2
class RestaurantePaia:
    nome = ''
    categoria = ''
    ativo = False
    dono = ''
    periodo = ''

restPaia1 = RestaurantePaia()
restPaia1.nome = 'Julia'
restPaia1.categoria = 'Vegano'
restPaia1.dono = 'Julia'
restPaia1.periodo = 'Tarde'
funcaolegal('2',restPaia1)

# Questão 3
class Restaurante:
    def __init__(self,nome,categoria,dono,periodo):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False
        self.dono = dono
        self.periodo = periodo

rest1 = Restaurante('Lo Cartel de medelim','Comida Colombiana',"Pablo Escobar","Integral")
funcaolegal('3',rest1)

# Questão 4
class Restaurante2:
    def __init__(self,nome,categoria,dono,periodo):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False
        self.dono = dono
        self.periodo = periodo
    
    def __str__(self):
        return f'{self.nome.ljust(15)} | {self.categoria.ljust(15)} | {self.dono.ljust(15)} | {self.periodo}'

rest2 = Restaurante2('Lo Cartel de medelim','Comida Colombiana',"Pablo Escobar","Integral")
print('')
print('Questão 4')
print(rest2)
print('')

class Cliente:
    def __init__(self,nome,sobrenome,idade,genero):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.idade = idade
        self.genero = genero

cliente1 = Cliente('Bebete','Rodrigues',20,'Feminino')
funcaolegal('5',cliente1)