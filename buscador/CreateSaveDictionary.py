
from create_index import create_matrix, youmean
import pickle

#Se o csv das noticias for alterado, pode-se, nesse arquivo criar um novo indice invertido.

all_words, dict = create_matrix()
with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(dict, f)
        