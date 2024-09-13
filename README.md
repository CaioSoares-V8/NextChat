# NextChat

## Descrição
Este projeto é uma aplicação de chatbot desenvolvida em Python, integrada ao terminal de linha de comando, que utiliza a API Groc para enviar requisições a uma inteligência artificial e gerar respostas dinâmicas durante as conversas com os usuários. O chatbot oferece funcionalidades como consulta ao histórico de interações, permitindo que os usuários revisitem conversas anteriores. A aplicação é executada de forma isolada em um ambiente virtual Python (VENV), garantindo uma configuração de dependências independente e segura.


## Índice
1. [Tecnologias Utilizadas](#tecnologias-utilizadas)
2. [Instalação](#instalação)
3. [Como Usar](#como-usar)
4. [Dicas Bônus](#dicas-bonus)


## Tecnologias Utilizadas
- Linguagem de progamação: Python
- API: Groc
- Ambiente virtual: (VENV)
- Bibliotecas: requests, python-dotenv, colorama
- Interface de desenvolvimento: VSCode


## Instalação
Instruções para configurar o ambiente local e rodar o projeto.

```bash
# Clone o repositório
git clone https://github.com/CaioSoares-V8/NextChat.git

# Crie um ambiente virtual
python -m venv venv

# Acesse esse ambiente
venv\Scripts\activate.bat

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente do arquivo .env
API_URL = 'https://api.groq.com/openai/v1/chat/completions'
API_KEY = #Insira sua CHAVE DA API

# Execute a aplicação
python app.py
```

## Como usar
Ao iniciar a aplicação, você já estará apto a realizar perguntas ou explorar as outras funcionalidades do NextChat.

Digite <b>HISTÓRICO</b> para acessar os dados referentes à pergunta e resposta das suas últimas interações no chat.

Digite <b>RESET</b> para limpar esse histórico.

Digite <b>EXIT</b> para fechar a aplicação.

## Dicas bônus
Abaixo, segue um compilado de 5 dicas, construído com o auxílio do próprio NextChat, sobre como explorar melhor suas perguntas a uma inteligência artificial:

<b>Defina o Escopo com Precisão:</b> É fundamental definir com clareza o que você quer da IA. Evite vaguidão, indicando especificamente o tema ou objetivo.<br> 
<i style='color:grey'>Exemplo: Em vez de "Explique sobre ciência", pergunte "Explique o conceito de entropia na termodinâmica."</i>

<b>Use Instruções Passo a Passo:</b> A IA responde melhor quando a solicitação é dividida em etapas. Se uma pergunta envolve várias partes, oriente a IA para seguir uma sequência. <br>
<i style='color:grey'>Exemplo: "Primeiro, defina o conceito de blockchain; em seguida, descreva um caso de uso prático."</i>

<b>Inclua Formatos de Resposta:</b> Indicar o formato desejado ajuda a IA a gerar respostas estruturadas e eficientes. <br>
<i style='color:grey'>Exemplo: "Liste as três principais características da IA em formato de bullet points."</i>

<b>Dê Contexto e Restrições:</b> A IA responde melhor quando entende o contexto ou as limitações da pergunta. Forneça informações relevantes ou especifique os limites da resposta. <br>
<i style='color:grey'>Exemplo: "Explique a diferença entre machine learning e deep learning em menos de 100 palavras."</i>

<b>Refine com Feedback Iterativo:</b> Ajude a IA a ajustar perguntas após uma resposta inicial. Se a IA não fornecer a resposta esperada, refine a solicitação com base no feedback.
<br> 
<i style='color:grey'>Exemplo: "A resposta foi muito genérica. Pode detalhar mais sobre os algoritmos específicos usados em machine learning?"</i>

