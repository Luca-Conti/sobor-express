import os
from colorama import Fore, Style
from modolos.restaurante import Restaurante
restalrentes = Restaurante('Praça', 'Gourme')
def exibir_nome_do_programa():
        print(Fore.RED + """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""" + Fore.RESET)

def exibir_funcao():
    print('1. Cadastra restalrente')
    print('2. Listar restalrente')
    print('3. Alterna status do restaurante')
    print('4. Sair\n')

def subtitulo(texto):
    os.system('cls')
    linha =Fore.RED + Style.BRIGHT +  '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha + Fore.RED + Style.RESET_ALL)
    print()

def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal.')
    os.system('cls')
    main()

def opcao_invalida():
    subtitulo(texto = 'Opção invalida')
    voltar_menu_principal()

def novo_restalrante():
    '''Essa Função é responsavel pro cadatranovo restaurante
    
    inputs
    -Nome do restaurantes
    -Categoria

    -outout 
      adicionanovos resaurantes a lista

    '''
    subtitulo(texto = 'Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante_cadastro = input(f'qual a cadegoria do restaurante {nome_do_restaurante}: ')

    restaurentes = Restaurante(nome_do_restaurante, categoria_do_restaurante_cadastro)
    print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_reatalrante():
    subtitulo(texto = 'Listar Restaurantes')
    Restaurante.listar_restaurantes()
    voltar_menu_principal()

def aterar_estado_do_retaurante():
    subtitulo(texto='Alterando estado do restaurante')
    nome_restaurante = input('digite o nome do resturante que deseja alterar o estado: ')
    restaurante_encontadro = False
    for restaurante in restalrentes:
        if nome_restaurante == restaurante['nome']:
            print('retaurante encontrado')
            restaurante_encontadro = True
            restaurante['ativo'] = not restaurante['ativo']
            mesagem = f'o restaurante {nome_restaurante} foi ativo' if restaurante['ativo'] else f'o restaurante foi desativado'

            print(mesagem)

    if not restaurante_encontadro:
        print('o restaurante não foi encontrado')
    voltar_menu_principal()

def escolher_opcao():
    try:
        opicao_escolida = int(input('Escolha uma opcão: '))
        print(f'vc escolheu a opção {opicao_escolida}')

        if opicao_escolida == 1:
            novo_restalrante()
        elif opicao_escolida == 2:
            listar_reatalrante()
        elif opicao_escolida == 3:
            aterar_estado_do_retaurante()
        elif opicao_escolida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    subtitulo(texto = 'Finalizar app')

def main():
    exibir_nome_do_programa()
    exibir_funcao()
    escolher_opcao()

if __name__ == '__main__':
    main()