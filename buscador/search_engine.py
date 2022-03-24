# Aqui vai ficar o buscador de fato
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
import numpy as np
import pandas as pd
import pickle
from create_index import create_matrix, youmean, list_words

class SearchEngine:
    def __init__(self):

        #Abre o dicionario de index invertido
        with open('saved_dictionary.pkl', 'rb') as f:
            self.invertedIndex = pickle.load(f)
        self.df = pd.read_csv("compilado_noticias.csv")
        #Caso nao tenha o dicionario salvo pode mudar o parametro da funcao create_matrix para 1
        self.all_words, dicionario_errado = create_matrix(1)

    def ranquear(self, string_de_busca, n_max=10):

        #tenta achar a palvra no dicionario
        try:
            # print("voltei para ca")
            ret = []
            resultado = self.invertedIndex[string_de_busca]
            # print("esses sao os resultados \n", resultado)
            for e in resultado:
                
                noticia = self.df.iloc[[int(e[0])]]
                # print("adicionei mais um resultado a lista")
                ret.append(noticia["Titulo"].values)
            # print("estou retornando a lista", ret, string_de_busca)
            return ret, 0
        #se nao conseguir retorna a palavra mais proxima para que se possa fazer uma nova busca
        except:
            quizdizer = youmean(string_de_busca, self.all_words)
            return 0, quizdizer




