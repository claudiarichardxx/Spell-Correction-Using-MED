import pandas as pd
import urllib
import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
import sys
from Collections import Counter

def createData(link, filename = "data\\data.dat"):

  urllib.request.urlretrieve(link, filename)
  current_key = None
  result_dict = {}
  repeats = []
  print('About the spellcheck dataset:\n')
  data_file = open(filename, 'r')
  print(filename)
  for line in data_file.readlines():

      lines = line.strip().split('\n')

      if lines[0].startswith('$'):
              current_key = lines[0][1:].lower()
              if(current_key not in result_dict.keys()):
                  result_dict[current_key] = []
              else:
                print('The word "' + current_key + '" occurs more than once')
                repeats.append(current_key)
                #result_dict[current_key].append(lines[0].lower())
              #print(line[1:-2])
              #result_dict[current_key] = []
      else:
              result_dict[current_key].append(lines[0].lower())

  df = pd.DataFrame([result_dict.keys(), result_dict.values()]).T
  df.columns = ['words', 'misspellings']

  return df, repeats

def countWords(lst):
  return len(lst)

def describeData(df, repeats, word_count):
  
  df['num_of_words'] = df['misspellings'].apply(countWords)
  print('\nThere are a total of', len(df), 'unique correct words and', len(repeats) , 'repeats which totals to', len(df) + len(repeats),'words')
  print('There are a total of', df.num_of_words.sum(), 'misspelt words in the dataset')
  print('\nAbout the wordnet dictionary:\n')
  print('There are', word_count,'words in the wordnet dictionary\n')

def buildDictionary():
  
  dictionary = {}
  count = 0
  for word in wn.words(lang='eng'):

    if (word[0].lower() not in dictionary.keys()):
        dictionary[word[0].lower()] = set()

    dictionary[word[0].lower()].add(word.lower())
    count = count +1
    
  for i in dictionary.keys():
        dictionary[i] = sorted(dictionary[i], key=len)

  return dictionary, count

def findStarters(words, misspellings, pos):
  for i in misspellings:
      target = words[0]
      present = i[0]
      if (present not in pos.keys()):
          pos[present] = []
          #count = count + 1
      pos[present].append(target)
  return len(misspellings)

def findPossibleFirstLetters(df):
  pos = {}
  df['num_of_words'] = df.apply(lambda x: findStarters(x.words, x.misspellings, pos), axis = 1)
  for i in pos.keys():
    ll = Counter(pos[i])
    pos[i] = sorted(ll, key = ll.get, reverse = True)
  return df, pos