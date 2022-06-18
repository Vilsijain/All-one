import random
import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet

def generate_synonyms(word):
    synonyms = []
    result = set()
    for syn in wordnet.synsets(word):
            for each_lemmas in syn.lemmas():
                synonyms.append(each_lemmas.name())
            for each_synonym in synonyms: 
                result.add(each_synonym.replace('_', ''))
    return list(result)
                 
def generate_tlds(word):
    result=[]
    str2 = ['.com', '.in', '.co', '.net', '.org', '.co', '.info', '.me', '.website', '.tech','.host', '.cricket']
    for i in random.sample(str2,4):
        strres=word+i
        result.append(strres)
    return list(result)

 
def generate_prepended_strings(word):
    result=[]
    str2 = ['ve', 'bright', 'toffee', 'code', 'community', 'dev', 'eat', 'drink', 'repeat']
    for i in random.sample(str2,5):
        strfin=i+word
        result.append(strfin) 
    return list(result)

 
def generate_appended_strings(word):
    result=[]
    str2 = ['ve', 'bright', 'toffee', 'code', 'community', 'dev', 'eat', 'drink', 'repeat']
    for i in random.sample(str2,5):
        strfin=word+i
        result.append(strfin) 
    return list(result)

 
def generate_replaced_strings(word):
    final =  [char for char in word]

    final = ['ee' if x=='e' else x for x in final]
    final = ['z' if x=='s' else x for x in final]

    f1 = "".join(map(str,final))
    return  f1 
