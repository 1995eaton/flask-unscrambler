from flask import Flask, request, render_template
import os
import csv

app = Flask(__name__)

dictionary = {key: value for key, value in csv.reader(open("dictionary"))}


@app.route('/', methods=['GET', 'POST'])
def unscrambleWord():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        key = ''.join(sorted(''.join([i for i in request.form['letters'].lower() if i.isalpha()])))
        try:
            return dictionary[key]
        except KeyError:
            return ""

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        raise SystemExit
