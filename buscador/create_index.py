import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import numpy as np
from Levenshtein import distance as lev
import json


def create_matrix(opcao):
    comp_noticias = pd.read_csv("compilado_noticias.csv")
    noticias = comp_noticias.Noticias

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(noticias)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    df["Document"] = df.index
    all_words = []
    dict = {}
    if opcao == 0:
        for (index, colname) in enumerate(df):
            novo_df = pd.DataFrame()
            novo_df["Document"] = df["Document"].values
            novo_df[colname] = df[colname].values
            novo_df = novo_df.sort_values(by=[colname], ascending = False)

            tuples = [tuple(x) for x in novo_df.values]
            dict[colname] = tuples[:10]


        # json_object = json.dumps(dict, indent = 4)
        
        # # Writing to sample.json
        # with open("sample.json", "w") as outfile:
        #     outfile.write(json_object)


        for (index, colname) in enumerate(df):
            all_words.append(colname)
        return all_words, dict

    elif opcao == 1:
         for (index, colname) in enumerate(df):
            all_words.append(colname)

    return all_words, dict


def list_words(df):
    all_words = []
    for (index, colname) in enumerate(df):
        all_words.append(colname)
    return all_words



def youmean(pesquisa, all_words):
    menor_score = 10
    quizdizer = ""
    for e in all_words:
        score = lev(e,pesquisa)
        if score <= menor_score:
            menor_score = score
            quizdizer = e

    return quizdizer

# all_words, matri = create_matrix()

# print(matri["putin"])