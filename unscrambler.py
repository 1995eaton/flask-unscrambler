from flask import Flask, request
import os
import csv

app = Flask(__name__)

dictionary = {key: value for key, value in csv.reader(open("dictionary"))}

@app.route('/unscramble', methods=['POST'])
def unscrambleWord():
    key = ''.join(sorted(''.join([i for i in request.form['letters'].lower() if i.isalpha()])))
    try:
        return dictionary[key]
    except KeyError:
        return ""

if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        raise SystemExit
