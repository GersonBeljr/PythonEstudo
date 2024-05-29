import os 
# docstring
restaurantes = [{'nome':'Popo pães','categoria':'Padaria','ativo':False},
                {'nome':'Cidade de minas','categoria':'Mineiro','ativo':False},
                {'nome':'Miamoto','categoria':'Japones','ativo':False},
                {'nome':'Luigis','categoria':'Italiano','ativo':False}]
                

def exibir_maracutaia():
    print('''
 ______  ______  ______  ______  ______       ______ __  __  ______ ______  ______  ______  ______    
/\  ___\/\  __ \/\  == \/\  __ \/\  == \     /\  ___/\_\_\_\/\  == /\  == \/\  ___\/\  ___\/\  ___\   
\ \___  \ \  __ \ \  __<\ \ \/\ \ \  __<     \ \  __\/_/\_\/\ \  _-\ \  __<\ \  __\  \___  \ \___  \  
 \/\_____\ \_\ \_\ \_____\ \_____\ \_\ \_\    \ \_____/\_\/\_\ \_\  \ \_\ \_\ \_____\/\_____\/\_____\ 
  \/_____/\/_/\/_/\/_____/\/_____/\/_/ /_/     \/_____\/_/\/_/\/_/   \/_/ /_/\/_____/\/_____/\/_____/  \n''')

def definiropcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair \n')

def voltar_menu():
    input('\ndigite uma tecla para retornar ao menu')
    main()

def opc_invalida():
    print('opção invalida \n')
    voltar_menu()

def cadastrar_novo_restaurante():
    '''Essa função ela destroi familias e o mundo todo muahahahahhahahaha espero que use com cuidado... mentira ela só adiciona um novo restaurante dentro do dicionario restaurantes'''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria = input(f'Informe a categoria do Restaurante {nome_restaurante}: ')
    print('Qual a situação do restaurante?\nAtivo = 1\nInativo = 2')
    status = input('Defina o status do restaurante: ')
    status = True if status == "1" else False
    dados_restaurante  = {'nome':nome_restaurante,'categoria':categoria,'ativo':status}
    restaurantes.append(dados_restaurante)
    print(f'\n Restaurante {nome_restaurante} cadastrado com sucesso')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes\n')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria_restaurante=restaurante['categoria']
        atividade_restaurante= 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {atividade_restaurante}')

    voltar_menu()
        
def alterar_status():
    exibir_subtitulo('Alterando status do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante a ser alterador: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi {'ativado' if restaurante["ativo"] else 'inativado'} com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado')

    voltar_menu()

def fechar_app():
    exibir_subtitulo('App finalizado')
    print('Sabor Express aprecia sua visita\n - volte sempre')

def exibir_subtitulo(texto):
    os.system("cls")
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def escolher_opc():
    try:
        opc_escolhida = int(input("Escolha uma opção: "))

        if opc_escolhida==1:
            cadastrar_novo_restaurante()
        elif opc_escolhida==2:
            listar_restaurantes()
        elif opc_escolhida==3:
            alterar_status()
        else:
            fechar_app()
    except:
        opc_invalida()

def main():
    os.system("cls")
    exibir_maracutaia()
    definiropcoes()
    escolher_opc()

if __name__ == '__main__':
    main()