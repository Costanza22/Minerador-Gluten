Mineração de Textos Científicos em Python: Um Guia Detalhado

**Tema TCC: Sistema de Detecção de Contaminação em Alimentos sem Glúten utilizando Inteligência Artificial**

Todos os artigos são voltados ao Portifólio!

**Objetivo**

Deixar os consumidores celíacos mais confiantes em relação a contaminação cruzada em alimentos classificados como "sem glúten"
Em grandes redes de supermercados é comum que no setor sem glúten mesmo que pouco percebido tenha alimentos que originalmente é sem glúten mas durante o seu processsamento acabou sendo contaminado por exemplo "Sem Glúten, alérgicos contêm Cevada" isso gera uma certa falta de confiança por parte dos consumidores.
A ideia de implementar uma ia que possa lidar com esse tipo de situação e achar uma solução utilizando ferramentas de aprendizagem de máquina.

Este repositório contém um guia completo para desenvolver um sistema de mineração de textos científicos em Python. O sistema permite extrair dados de artigos,como títulos, resumos, autores, datas de publicação e palavras-chave, e realizar análises de processamento de linguagem natural (PLN) para extrair informações valiosas.

**Funcionalidades:**

Coletar dados: O sistema se concentra na coleta de dados do ScienceDirect, um portal de periódicos renomado com acesso a uma vasta coleção de artigos científicos.
Além disso, em adição portais como o Kaggle e Periodicos da própria universidade foram complementados.

Processamento de linguagem natural: O sistema utiliza técnicas de PLN para pré-processar, tokenizar, lematizar e remover palavras de parada dos textos em inglês.

Análise de frequência: O sistema identifica as palavras mais frequentes nos textos e apresenta uma visualização em nuvem de palavras.

Extração de termos-chave: O sistema extrai os termos-chave mais relevantes dos textos para auxiliar na categorização por tema.

Análise de sentimento: O sistema determina se o sentimento geral dos textos é positivo, negativo ou neutro em relação ao tema.

Nuvens de palavras e redes de palavras: O sistema gera visualizações para as palavras mais frequentes e suas relações.


Personalização: O sistema pode ser personalizado para incluir diferentes critérios de busca e análises.

**Requisitos:**

Python 3.10 ou superior: A linguagem de programação base para o sistema.

**Bibliotecas:**

requests: Para realizar requisições HTTP ao ScienceDirect.
BeautifulSoup: Para extrair dados das páginas HTML do ScienceDirect.
pandas: Para manipular e analisar dados.
nltk ou spaCy: Para processamento de linguagem natural dos textos em inglês.
matplotlib ou seaborn: Para visualização de dados.
Conta no ScienceDirect: Crie uma conta no ScienceDirect para ter acesso à API e coletar dados.
Ambiente de Desenvolvimento: Um editor de código como PyCharm ou Visual Studio Code e uma ferramenta de análise de dados como Jupyter Notebook.

**Como Usar:**

Clone o Repositório: Clone este repositório em seu computador local.

Instale as Bibliotecas: Execute o comando pip install -r requirements.txt no terminal para instalar as bibliotecas necessárias.
Configure o ScienceDirect: No arquivo config.py, defina as credenciais de acesso à API do ScienceDirect (API Key e Token).
Defina os Critérios de Busca: No arquivo config.py, defina as palavras-chave, data de publicação e outros critérios para a busca de artigos.
Execute o Script: Execute o script main.py para coletar, processar e analisar os dados dos artigos científicos do ScienceDirect.
Explore os Resultados: Os resultados das análises serão salvos em arquivos CSV e visualizações serão geradas automaticamente.
