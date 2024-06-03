# 1 criar uma classe restaurante

class restaurante:
    nome = ''
    categoria = ''
    ativo = False

# 2 criação de objetos

rest_praca = restaurante()
rest_praca.nome = 'praca'

# atividade 1 

rest_praca.categoria = 'italiana'

# atividade 2 

restQ1 = rest_praca.nome
print(restQ1)

# atividade 3 

print(f'O restaurante {rest_praca.nome} está {'Ativo' if rest_praca.ativo else 'Inativo'}')

# atividade 4 

categoria = restaurante.categoria

# atividade 5 

restaurante.nome = 'bistro'

# atividade 6 

rest_pizza = restaurante()
rest_pizza.nome = 'Pizza Place'
rest_pizza.categoria = 'Fast Food'

# atividade 7 

print(f'{'A categoria é Fast Food' if  rest_pizza.categoria == 'Fast Food' else 'A categoria não é Fast Food' }')

# atividade 8 

rest_pizza.ativo = True

# atividade 9 

print(f'O restaurante {rest_praca.nome} tem categoria {rest_praca.categoria} ')
