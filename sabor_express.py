import os

lista_restaurantes = [

                      {'nome':'norden', 'ramo':'cervejaria', 'ativo':True},
                      {'nome':'Rosa mexicana', 'ramo':'Mexicana', 'ativo':False},
                      {'nome':'Bier vila', 'ramo':'cervejaria', 'ativo':True}
                        
                    ]

def exibir_nome_do_programa():
    print("""
          

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  

    """)

def exibir_opcoes():
    print('Escolha um serviço:\n')
    print('1.Restaurantes frnaquiados')
    print('2.Adicionar franquiado')
    print('3.Ativar restaurante')
    print('4.Sair dos serviços\n')

def sair_servico():
    exibir_subtitulo('Finalizando consulta')
    

def servico_invalido():
    print('\n Voce digitou uma opção invalida\n')
    volta_menu()

def volta_menu():
     input('\n Pressione enter para voltar ao menu principal')
     main()

def alternar_estado():
    exibir_subtitulo('Mudando o estado do restaurante')
    nome_restaurante = input('Informe o nome do restaurante que deseja mudar o estado:')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado ' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            volta_menu()

    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')
        volta_menu()
     
def exibir_subtitulo(texto):
    os.system('cls') 
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():    
    exibir_subtitulo('Cadastrando restaurantes')
    nome_restaurante = input('Insira o nome do restaurante: \n')
    ramo_restaurante = input('Informe o ramo do restaurante: \n')
    informações_restaurante = {'nome':nome_restaurante, 'ramo':ramo_restaurante, 'ativo':False}
    lista_restaurantes.append(informações_restaurante)
    print(f'Restaurante {nome_restaurante}, foi cadastrado\n')
    volta_menu()


def exibir_restaurantes():
    exibir_subtitulo('Exibindo restaurantes')

    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in lista_restaurantes:
        nome = restaurante['nome']
        ramo = restaurante['ramo']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'

        print(f'-{nome.ljust(20)} | {ramo.ljust(20)} | {ativo.ljust(20)}')
    volta_menu()


def escolher_servico():
    try:
        servico_escolhido = int(input('Escolha um serviço:'))

        if servico_escolhido == 1:
            exibir_restaurantes()
        elif servico_escolhido == 2:
            cadastrar_restaurante()
        elif servico_escolhido == 3:
            alternar_estado()
        elif servico_escolhido == 4:
            sair_servico()
        else:
            servico_invalido()
    except:
            servico_invalido()    


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_servico()
    
    


if __name__ == '__main__':
    main()
