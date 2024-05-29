# API_Twitter_Estudo
Projeto de estudos em andamento para API

#Códigos disponivel nesse diretório

Introdução
Neste projeto prático, vamos desenvolver uma aplicação que consome a API REST do Twitter para coletar dados, analisar esses dados e criar relatórios e dashboards amigáveis. A aplicação será containerizada usando Docker e modularizada para facilitar a manutenção e escalabilidade.

Pré-requisitos
Twitter Developer Account
Para utilizar a API do Twitter, você precisa de uma conta de desenvolvedor no Twitter. Isso permitirá que você crie um aplicativo no Twitter e obtenha as credenciais necessárias para acessar a API.

Credenciais de API do Twitter
Após criar a conta de desenvolvedor, você precisará gerar as seguintes credenciais:

API Key
API Secret Key
Bearer Token
Ambiente de Desenvolvimento
Para seguir este tutorial, você precisará ter instalado:

Python 3.8 ou superior
Docker
Docker Compose
Estrutura do Projeto
A estrutura do projeto será organizada da seguinte forma:

arduino
Copiar código
twitter-dashboard/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── data_collection.py
│   ├── data_processing.py
│   ├── data_visualization.py
│   └── config.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_data_collection.py
│   ├── test_data_processing.py
│   ├── test_data_visualization.py
│   └── test_config.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

Crie um arquivo requirements.txt com as seguintes dependências:

requests
pandas
matplotlib
seaborn
plotly
dash
flask

Conclusão
Neste projeto, desenvolvemos uma aplicação para consumir a API do Twitter, processar e analisar os dados, e exibir os resultados em relatórios e dashboards. 
Containerizamos a aplicação com Docker e modularizamos o código para melhor manutenção e escalabilidade.


