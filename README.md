# Spell-Correction-Using-MED
A system to evaluate the Minimum Edit Distance(MED) algorithm for spelling correction on spellcheck datasets from https://www.dcs.bbk.ac.uk/~roger/corpora.html (birkbeck, aspell and wikipedia).

# To setup the environment:
To  install the required libraries, run this:
```
pip install -r requirements.txt
```

# How to run:
To replicate our results on the birkbeck dataset or to test the program for aspell or wikipedia datasets, you can use the main.py file. 
The main.py file calls a function called 'findingClosestWords'
Arguments:
1. start_index : default = 1 
2. end_index   : default = 5, 
3. k_vals      : default = [1,5,10]
4. link        : default = links['birkbeck'] ; available: links['aspell'], links['wikipedia']
5. df          : Optional, you can pass a pandas dataframe with columns 'words' and '' 

# To reproduce the results on Birkbeck:

The program was run on multiple systems and the results were stored as json files. They are available in resuls\parts. We import the result files in the example run(examples\spellCheckUsingMED.ipynb) to show the calculation of the s@k metric.

# Folders:

1. Example run can be found in examples\
2. Functions used are in utils\ and run.py
3. main.py is the file you should be running, change the parameters
4. data\ is where the data is stored
5. results\birkbeckResults has results from our run 

# Optimizations:
To optimize the time complexity of the algorithm, we implemented the following:

1. All words with the same MED were given the same rank
2. The MED between the correct and misspelled token is the maximum possible rank. Therefore, the search exits when all the positions before the maximum possible rank are taken. For example: Maximum rank is 3. If we find words in the dictionary with MED 2 and 1, the search exits, even if all the words haven't been checked.
3. A list of possible starting letters for every start letter in the misspelled words is obtained to narrow down the search.
4. The words in wordnet are stored as a dictionary (hashmap) with the starting letter as the key
5. The python package 'pandarallel' is utilized for parallel processing


# Evaluation Metric:
s@k : This denotes the rank of the correct word among other matches in the dictionary



