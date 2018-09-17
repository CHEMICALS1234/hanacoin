from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)
global fuck
fuck = 10
while True:
    fuck += 10
    time.sleep(1)

@app.route('/')
def bindex():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

    email = request.form['email']
    name = request.form['name']
    check = request.form['check']


    if name and email and check:
        Neo_name = name[::-1]

        return jsonify({'name' : Neo_name})

    return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.run()