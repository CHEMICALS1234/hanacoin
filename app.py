from flask import Flask, render_template, request, jsonify, json, g
import time
from economy import money
app = Flask(__name__)


@app.route('/')
def bindex():
    for x in money():
        g = x
    return render_template('form.html')

@app.route('/process', methods=['POST'])

def process():
    return str(g)

if __name__ == '__main__':
    app.run(debug=True)