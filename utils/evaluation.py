from collections import Counter

def getResults(df):

  k_values = []
  for row in df['k_list']:
      k_values.extend(row)
  results = Counter(k_values)
  for i in results.keys():
    print('k = ', i,'in', results[i], 'search(es)')

  return results


def getAverageSuccessValues(results, total, k_vals):

  success_at_k = {}
  for i in range(0, len(k_vals)):
    success_at_k[k_vals[i]] = 0
    for j in results.keys():
          till = k_vals[i]
          start = 0
          if(j > start and j<= till):
            success_at_k[k_vals[i]] += results[j]

  for i in success_at_k.keys():
    success_at_k[i] = round( success_at_k[i]/total * 100, 2)
    print('Success at', i, 'is', success_at_k[i],'%')

  return success_at_k



