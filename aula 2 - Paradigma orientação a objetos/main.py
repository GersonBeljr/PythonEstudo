from modelos.restaurante4 import Restaurante
import os 

rest = {}

def exibir_titulo():
    print('Sabor Express 2.0')
    
def exibir_opc():
    print('\n1. Listar Restaurantes')
    print('2. Registrar Restaurante')
    print('3. Avaliar Restaurante')
    print('4. Alterar status do restaurante')
    print('5. Sair\n')

def input_opc():
    try:
        opc_escolhida = int(input("Escolha uma opção: "))

        if opc_escolhida==1:
            listar_rest()
        elif opc_escolhida==2:
            registrar_rest()
        elif opc_escolhida==3:
            avaliar_rest()
        elif opc_escolhida==4:
            alterar_status()
        elif opc_escolhida==5:
            sair()
        elif opc_escolhida==6:
            test()
        else:
            print('\n OPÇÃO INVALIDA, TENTE NOVAMENTE\n')
            input_opc()
            
    except:
        print('ERRO')
        sair()
        
def listar_rest():
    print('Lista dos restaurantes\n')
    Restaurante.listar_restaurantes()
    
    voltar_menu()
    
def registrar_rest():
    print('Registrar novo restaurante\n')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria = input('Digite aqui a categoria desse novo restaurante: ')
    rest[nome_restaurante] = Restaurante(nome_restaurante,categoria)
    voltar_menu()
    
def avaliar_rest():
    print('Avaliação de restaurantes\n')
    nome_restaurante = input('Digite aqui o nome do restaurante avaliado: ')
    for restaurante in Restaurante.restaurantes:
        if rest[nome_restaurante]._nome == restaurante._nome:
            print('Restaurante encontrado\n')
        else:
            print('Restaurante não encontrado tente novamente')
            avaliar_rest()
    avaliador = input('Qual o nome de quem fez a avaliação?: ')
    nota = int(input("De uma nota de 0 a 10: "))
    rest[nome_restaurante].receber_avaliacao(avaliador,nota)
    print(f'A media das avalições do restaurante {nome_restaurante} é {rest[nome_restaurante].media_avaliacoes}')
    
    voltar_menu()
    
def alterar_status():
    print('Alterar status de restaurante\n')
    
    nome_restaurante = input('Digite aqui o nome do restaurante para alterar o status: ')
    for restaurante in Restaurante.restaurantes:
        if rest[nome_restaurante]._nome == restaurante._nome:
            print('Restaurante encontrado\n')
        else:
            print('Restaurante não encontrado tente novamente')
            alterar_status()
    rest[nome_restaurante].alternar_estado()
    voltar_menu()

def voltar_menu():
    input('\ndigite uma tecla para retornar ao menu')
    main()
  
def sair():
    print('App finalizado')
    print('Sabor Express 2.0 aprecia sua visita\n - volte sempre\n')


def test():
    for restaurante in Restaurante.restaurantes:
        print(restaurante._nome)
        nome_restaurante = input('nome: ')
        print(rest[nome_restaurante]._nome)
        print(restaurante._nome == rest[nome_restaurante]._nome)


def main():
    os.system("cls")
    exibir_titulo()
    exibir_opc()
    input_opc()
     
if __name__ == '__main__':
    main()
