import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import requests
from bs4 import BeautifulSoup

# URL do artigo
url_artigo = "https://www.sciencedirect.com/science/article/pii/S0950329324000855"

# Acessando o artigo
response = requests.get(url_artigo)
soup = BeautifulSoup(response.content, 'html.parser')

# Título do artigo
titulo = soup.find('h1', class_='sv-title').text

# Autores do artigo
autores = [autor.text for autor in soup.find_all('a', class_='author')]

# Resumo do artigo
resumo = soup.find('p', class_='abstract-text').text

# Corpo do artigo (opcional)
if 'body-text' in soup.find('div', class_='article-content').attrs:
  corpo_artigo = soup.find('div', class_='article-content')['body-text']
else:
  corpo_artigo = None

#chaves
'Non-celiac consumers'
'Measures'

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Pré-processamento
texto = corpo_artigo.lower()  # Converter para minúsculas
texto = re.sub(r'[^\w\s]', '', texto)  # Remover caracteres especiais
palavras = word_tokenize(texto)  # Tokenizar o texto em palavras
stop_words = set(stopwords.words('english'))  # Obter palavras de parada em inglês
palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_words]  # Remover palavras de parada
lematitzador = WordNetLemmatizer()  # Criar um lematizador
palavras_lematizadas = [lematitzador.lemmatize(palavra) for palavra in palavras_filtradas]  # Lematizar as palavras

# Análise de frequência
frequencia_palavras = nltk.FreqDist(palavras_lematizadas)
palavras_mais_comuns = frequencia_palavras.most_common(20)  # Obter as 20 palavras mais comuns

# Visualização (opcional)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(palavras_mais_comuns[:10], [frequencia for frequencia, _ in palavras_mais_comuns[:10]])
plt.xlabel('Palavras')
plt.ylabel('Frequência')
plt.title('Frequência das 10 Palavras Mais Comuns')
plt.show()
