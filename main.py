import nltk
import pandas as pd
from run import SpellCheck
from pandarallel import pandarallel
nltk.download('wordnet')


if __name__ == "__main__":

    sp  = SpellCheck()
    pandarallel.initialize(nb_workers = 300)
    links = { 'birkbeck' : 'https://www.dcs.bbk.ac.uk/~roger/missp.dat',
        'aspell' : 'https://www.dcs.bbk.ac.uk/~roger/aspell.dat',
        'wikipedia' : 'https://www.dcs.bbk.ac.uk/~roger/wikipedia.dat' }
    k_values = sp.findingClosestWords(start_index = 1, end_index = 5, 
                                   k_vals = [1,5,10], link = links['birkbeck'])

