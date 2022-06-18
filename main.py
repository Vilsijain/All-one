#AI powerd word suggestion
import os
from flask import Flask,jsonify
from flask_cors import cross_origin

from utils import (
        generate_appended_strings,
        generate_prepended_strings,
        generate_replaced_strings,
        generate_synonyms,
        generate_tlds,
)

app = Flask(__name__)

@app.route("/<string:word>",methods=["GET","OPTIONS"])
@cross_origin()
def generate_all(word):
    generators = {
                    'synonyms': generate_synonyms,
                    'append': generate_appended_strings,
                    'prepend': generate_prepended_strings,
                    'replaced': generate_replaced_strings,
                    'tlds': generate_tlds
                }
    result = {}
    for op,fn in generators.items(): 
            result[op] = fn(word)
    return jsonify(result)
    
if __name__ == '__main__':
    
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port)
