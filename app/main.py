from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    html = "<h3>Hello Miguel Del Moral</h3>"
    return html.format(format)

def recursive_fibonacci(n):
    if n<0: 
        LOG.error("Incorrect input")
        return 0
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2) 

@app.route("/fibonacci", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:
        {
            "value": 0
        }
        
        result looks like:
        { 
            "fibonacci": 0 
        }
        
    """
    
    # Logging the input payload
    json_payload = request.json
    n = int(json_payload["value"])
    LOG.info(n)
    
    return jsonify({'fibonnaci': recursive_fibonacci(n)})

if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0')
