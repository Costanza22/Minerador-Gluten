import re
import pandas as pd  # Manipulação de dados em formato tabular
import numpy as np  # Operações matemáticas com arrays
import nltk  # Processamento de Linguagem Natural (PLN)
from nltk.corpus import stopwords  # Palavras de parada em português
from nltk.tokenize import word_tokenize  # Tokenização de texto
from nltk.stem import PorterStemmer  # Stemmer para reduzir palavras à raiz
from sklearn.feature_extraction.text import TfidfVectorizer  # Vetorização TF-IDF
from sklearn.decomposition import LatentDirichletAllocation
dados = pd.read_csv("C:\Users\costanza\Desktop\celiac.xlsx")
# Limpeza dos textos
def limpar_texto(texto):
  """
  Função para limpar e normalizar o texto.

  Argumentos:
    texto (str): Texto a ser limpo.

  Retorno:
    str: Texto limpo e normalizado.
  """
  texto = texto.lower() 
  texto = re.sub(r'[^\w\s]', '', texto) 
  texto = word_tokenize(texto)
  palavras_stop = set(stopwords.words('portuguese'))  
  texto = [palavra for palavra in texto if palavra not in palavras_stop]  
  stemmer = PorterStemmer() 
  texto = [stemmer.stem(palavra) for palavra in texto]  
  texto = ' '.join(texto) 
  return texto
dados['texto_limpo'] = dados['texto'].apply(limpar_texto)
vetorizador = TfidfVectorizer()
matriz_tfidf = vetorizador.fit_transform(dados['texto_limpo'])

from matplotlib import pyplot as plt
n_topicos = 10  
modelo_lda = LatentDirichletAllocation(n_components=n_topicos)
modelo_lda.fit(matriz_tfidf)
termos_topicos = modelo_lda.components_
for i, tópico in enumerate(termos_topicos):
  plt.figure()
  plt.bar(vetorizador.get_feature_names(), tópico)
  plt.title(f"Tópico {i}")
  plt.show()




