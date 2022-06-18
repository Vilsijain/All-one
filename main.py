#AI powerd word suggestion
import os
from flask import Flask,jsonify
from flask_cors import cross_origin

from utils import * 

app = Flask(__name__)

@app.route("/<string:word>",methods=["GET","OPTIONS"])
@cross_origin()
def generate_all(word):
    generators = [generate_synonyms,
                 generate_appended_strings,
                 generate_prepended_strings,
                 generate_replaced_strings,
                 generate_tlds
                ]
    result = []
    for gen in generators: 
        result.extend(gen(word))
    print(result)
    return jsonify(result)
    
if __name__ == '__main__':
    
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port)
