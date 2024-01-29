#Importing necessary libraries from utils 
from utils.tools import DistanceTools
from utils.setup import SetupFunctions
from utils.evaluation import Evaluation
import json
import urllib.request
import pandas as pd
pd.options.mode.chained_assignment = None

class SpellCheck:

    def createData(self, link, filename = "./data//data.dat"):
        #Function to download the data from the link and create pandas dataframe
        urllib.request.urlretrieve(link, filename)
        current_key = None
        result_dict = {}
        repeats = []
        #print('About the spellcheck dataset:\n')
        for line in open(filename).readlines():

            lines = line.strip().split('\n')

            if lines[0].startswith('$'):
                    current_key = lines[0][1:].lower()
                    if(current_key not in result_dict.keys()):
                        result_dict[current_key] = []
                    else:
                        #print('The word "' + current_key + '" occurs more than once')
                        repeats.append(current_key)
                        #result_dict[current_key].append(lines[0].lower())
                    #print(line[1:-2])
                    #result_dict[current_key] = []
            else:
                    result_dict[current_key].append(lines[0].lower())

        df = pd.DataFrame([result_dict.keys(), result_dict.values()]).T
        df.columns = ['words', 'misspellings']

        return df, repeats


    def findingClosestWords(self, start_index = 0, end_index = 10, df =None, 
                          k_vals = [1,5,10], 
                          link =  "https://www.dcs.bbk.ac.uk/~roger/missp.dat"):

        #Function to find the closest words from the given list for the misspelled word
        tools = DistanceTools()
        setup = SetupFunctions()
        evals = Evaluation()
        repeats = []
        if (df is None):
            df, repeats = self.createData(link = link)  #can mention filename and link here

        df, starters = setup.findPossibleFirstLetters(df)
        dictionary, word_count = setup.buildDictionary()
        setup.describeData(df, repeats, word_count)
        df1 = df[start_index : end_index]
        df1['k_list'] = df1.parallel_apply(lambda x: tools.find_k(x.words, x.misspellings, dictionary, starters), axis = 1)
        results = evals.getResults(df1)
        print('\n')
        success_at_k = evals.getAverageSuccessValues(results, df1.num_of_words.sum(), k_vals)
        df1.drop(columns = ['num_of_words'], inplace = True)
        df1.to_json('spellCheck.json')
        with open("evalResults.json", "w") as fp:
            json.dump(success_at_k, fp)
        print('-----------------------------------------------------------------------------------------------------')
        return df1
