import requests
import os
from dotenv import load_dotenv
from colorama import Fore, Style

load_dotenv()
api_key = os.getenv('API_KEY')
api_url = os.getenv('API_URL')

class NextChat():
    historico_interacoes = []

    def enviar_pergunta(self, pergunta):
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
        "messages": [
                {
                    "role": "user",
                    "content": f"{pergunta}"
                }
            ],
            "model": "llama3-8b-8192"
        }

        requisicao = requests.post(api_url, json=data, headers=headers)
        conteudo = requisicao.json()
        resposta = conteudo['choices'][0]['message']['content']

        
        if (requisicao.status_code == 200):
            self.historico_interacoes.append({'Pergunta':f'{pergunta}', 'Resposta':f'{resposta}'})
            return resposta
        else:
            print(f'ERRO Status code: {requisicao.status_code}')

    @property
    def listar_interacoes(self):
        print(Fore.CYAN + '\nHISTORICO DE INTERAÇÕES:' + Style.RESET_ALL)
        if not self.historico_interacoes:
            print(Fore.CYAN + 'Historico vazio\n' + Style.RESET_ALL)
        for i, interacao in enumerate(self.historico_interacoes, start=1):
            pergunta = interacao['Pergunta']
            resposta = interacao['Resposta']
            print(Fore.CYAN + f'{i} - Pergunta: {pergunta.ljust(20)} | Resposta: {resposta}' + Style.RESET_ALL)
        print('')

    def limpar_historico(self):
        print(Fore.CYAN + '\nHistorico limpo\n' + Style.RESET_ALL)
        self.historico_interacoes = []                
        
    