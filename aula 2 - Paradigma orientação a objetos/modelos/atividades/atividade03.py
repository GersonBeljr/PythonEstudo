
# class Livro:
#     def __init__(self,titulo,autor,paginas):
#         self.titulo=titulo
#         self.autor=autor
#         self.paginas=paginas
#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'

#     def aumentar_paginas(self,quantidade):
#         self.paginas += quantidade

# livro1=Livro('Tanto Faz','Jão',50)
# print(livro1)
# print('')

# livro1.aumentar_paginas(90)
# print(livro1)
# print('')

# #   questão 1
# class Pessoa:
#     def __init__(self,nome,idade,profissao):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao
#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    
#     def saudacao(self):
#         if self.profissao:
#             print( f'Olá sou {self.nome}! Trabalho como {self.profissao}.')
#         else:
#             print( f'Olá, sou {self.nome}!')


#     def aniversario(self):
#         self.idade +=1

# pessoa1=Pessoa('Aparício',99,'programador')
# print(pessoa1)
# print('')
# pessoa1.aniversario()
# print(pessoa1)
# print('')
# pessoa1.saudacao()
# print('')

#  questão 2
# class ContaBancaria:
#     def __init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#         self._ativo=False #atributo protegido  
    
# # questão 3
#     def __str__(self):
#         return f'Conta de {self.titular} - Saldo: R${self.saldo}'

# # conta1=ContaBancaria('Nathan',3000.00)
# # conta2=ContaBancaria('Joe',2.00)

# # print(conta1)
# # print('')
# # print(conta2)

# # questão 4
#     @classmethod
#     def ativar_conta(cls,conta):
#         conta._ativo=True

# conta3=ContaBancaria('Arina',3.58)
# print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Depois de ativar: Conta ativa? {conta3._ativo}')

# # questão 5
# class ContaBancariaPythonica:
#     def __init__(self,titular,saldo):
#         self._titular=titular
#         self._saldo=saldo
#         self._ativo=False
    
#     @property
#     def titular(self):
#         return self._titular
    
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo
    
# # questão 6
# conta4=ContaBancariaPythonica('Josefino',1500.03)
# print(f'Titular da conta 4 é: {conta4.titular}')

# questão 7
class ClienteBanco:
    def __init__(self,nome,idade,profissao,endereco,telefone):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
        self.endereco=endereco
        self.telefone=telefone

# cliente1=ClienteBanco('João',30,'médico','Rua A','3696 6969')
# cliente2=ClienteBanco('Caio',19,'mecânico','Rua B','3696 6960')
# cliente3=ClienteBanco('Vitor',23,'programador','Rua C','3696 6965')

# questão 8

    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return conta

conta_cliente1=ClienteBanco.criar_conta('Tertulia',9999.99)
print(f'Conta de {conta_cliente1.titular} com saldo de R${conta_cliente1.saldo_inicial}')

