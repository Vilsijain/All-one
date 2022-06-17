#AI powerd word suggestion
import os
import random
from flask import Flask,jsonify
from flask_cors import cross_origin
import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet

app = Flask(__name__)

@app.get('/synonyms/<string:word>/')
@cross_origin() 
def generate_synonyms(word):
    synonyms = []
    result = set()
    for syn in wordnet.synsets(word):
            for each_lemmas in syn.lemmas():
                synonyms.append(each_lemmas.name())
            for each_synonym in synonyms: 
                result.add(each_synonym.replace('_', ''))
    if len(result) == 0:
        return jsonify({"message": "No synonyms found for the word {word}"})
    return jsonify(list(result))
                    

@app.route('/tlds/<string:words>/')
@cross_origin() 
def generate_tlds(words):
    result=[]
    str2 = ['.com', '.in', '.co', '.net', '.org', '.co', '.info', '.me', '.website', '.tech','.host', '.cricket']
    for i in random.sample(str2,4):
        strres=words+i
        result.append(strres)
    return jsonify(result)

@app.route('/prepend/<string:words>/')
@cross_origin() 
def generate_prepended_strings(words):
    result=[]
    str2 = ['ve', 'bright', 'toffee', 'code', 'community', 'dev', 'eat', 'drink', 'repeat']
    for i in random.sample(str2,5):
        strfin=i+words
        result.append(strfin) 
    return jsonify(result)


@app.route('/append/<string:words>/')
@cross_origin() 
def generate_appended_strings(words):
    result=[]
    str2 = ['ve', 'bright', 'toffee', 'code', 'community', 'dev', 'eat', 'drink', 'repeat']
    for i in random.sample(str2,5):
        strfin=words+i
        result.append(strfin) 
    return jsonify(result)


@app.route('/replace/<string:word>/')
@cors_origin() 
def generate_replaced_strings(word):
    final =  [char for char in word]

    final = ['ee' if x=='e' else x for x in final]
    final = ['z' if x=='s' else x for x in final]

    f1 = "".join(map(str,final))
    return f1

if __name__ == '__main__':
    
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port,debug=True)
