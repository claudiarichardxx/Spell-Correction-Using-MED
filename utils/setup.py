#This module initialises the data structure and metadata information required to run the algorithm
import pandas as pd
import urllib
import nltk
from nltk.corpus import wordnet as wn
#nltk.download('wordnet')
import sys
from collections import Counter

class SetupFunctions:
      
      def countWords(self, lst):
            #Function to get the number of words
            return len(lst)

      def describeData(self, df, repeats, word_count):
            #Function to describe the stats of the data
            print('About the dataset:\n')
            print('The following words are repeats: ')
            print(repeats)
            df['num_of_words'] = df['misspellings'].apply(self.countWords)
            print('\nThere are a total of', len(df), 'unique correct words and', len(repeats) , 'repeats which totals to', len(df) + len(repeats),'words')
            print('There are a total of', df.num_of_words.sum(), 'misspelt words in the dataset')
            print('\nAbout the wordnet dictionary:\n')
            print('There are', word_count,'words in the wordnet dictionary\n')

      def buildDictionary(self):
            #Function to dictionary data structure from the wordnet library
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
      
      def findStarters(self, words, misspellings, pos):
            #Function to make a list of the correct starting letter for each incorrect start to narrow down the search
            for i in misspellings:
                  target = words[0]
                  present = i[0]
                  if (present not in pos.keys()):
                        pos[present] = []
                        #count = count + 1
                  pos[present].append(target)

            return len(misspellings)
      
      def findPossibleFirstLetters(self, df):
            #Function to match and find the first letters from the wordnet 
            pos = {}
            df['num_of_words'] = df.apply(lambda x: self.findStarters(x.words, x.misspellings, pos), axis = 1)
            for i in pos.keys():
                  ll = Counter(pos[i])
                  pos[i] = sorted(ll, key = ll.get, reverse = True)
            return df, pos

