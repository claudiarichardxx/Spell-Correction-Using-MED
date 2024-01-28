from difflib import ndiff

def findTarget(target, word, dictionary, starters):

  max_length = len(target) + 10
  max_k = sum(levenshtein_distance_gen(target, word))

  temp = set([max_k])
  #print('The target is:', target)
  #print('The misspelt word is:', word)
  #print('Worst case k: ', max_k)

  if(max_k == 1):
    #print('k value is: ', max_k)
    return 1


  for start_letter in starters[word[0]]:
    #print('checking words starting with: ', start_letter)
    for w in dictionary[start_letter]:

      if (len(w) <= max_length):

          t = sum(levenshtein_distance_gen(word, w))
          if (t < max_k and t >0):
            #print('The check word is: '+ w +' , distance: ' + str(t))
            temp.add(t)

          if(len(temp) == max_k):
            #print(temp)
            #print('k value is: ', max_k)

            return max_k
      else:
        break
  #print(temp)
  #print('k value is: ', len(temp))
  return len(temp)

def levenshtein_distance_gen(str1, str2):

    counter = {"+": 0, "-": 0}
    for edit_code, *_ in ndiff(str1, str2):
        if edit_code == " ":
            yield max(counter.values())
            counter = {"+": 0, "-": 0}
        else:
            counter[edit_code] += 1
    yield max(counter.values())

def find_k(target, word_list, dictionary, starters):

  k_list = []
  for i in word_list:
      k_list.append(findTarget(target, i, dictionary, starters))

  return k_list
