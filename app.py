from nextchat import NextChat
from colorama import Fore, Style

chat = NextChat()

def encerrar_aplicacao():
    print(Fore.BLUE + '\nNextChat: Tchau!' + Style.RESET_ALL)
    print(Fore.BLUE + '\nAplicação Encerrada\n' + Style.RESET_ALL)

def exibir_resposta(resposta):
    print(Fore.BLUE + f'\nNextChat: {resposta}\n' + Style.RESET_ALL)
    realizar_pergunta()

def realizar_pergunta():
    pergunta = input('Voce: ')
    
    if pergunta == 'EXIT':
        encerrar_aplicacao()
    elif pergunta == 'HISTORICO':
        chat.listar_interacoes
        realizar_pergunta()
    elif pergunta == 'RESET':
        chat.limpar_historico()
        realizar_pergunta()
    else:
        resposta = chat.enviar_pergunta(pergunta)
        exibir_resposta(resposta)

def exibir_menu():
    print(Fore.BLUE + 
    '''
█▄░█ █▀▀ ▀▄▀ ▀█▀ █▀▀ █░█ ▄▀█ ▀█▀
█░▀█ ██▄ █░█ ░█░ █▄▄ █▀█ █▀█ ░█░
    ''')
    print('Seja bem vindo, fale com Next')
    print(
    '''
∙ digite HISTORICO para acessar as ultimas interações
∙ digite RESET para limpar o historico
∙ digite EXIT para sair
    ''' + Style.RESET_ALL)
        
def main():
    exibir_menu()
    realizar_pergunta()

if __name__ == '__main__':
    main()

