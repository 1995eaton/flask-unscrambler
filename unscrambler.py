from flask import Flask, request, render_template
from markupsafe import Markup
import os, csv
app = Flask(__name__)
dictionary = {key: value for key, value in csv.reader(open("dictionary"))}
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        anagram_input = ''.join([i for i in request.form['anagram_input'].lower() if i.isalpha()])
        try:
            r = dictionary[''.join(sorted(anagram_input))]
        except KeyError:
            return render_template('index.html', previous_anagrams = Markup(request.form['previous_anagrams']))
        return render_template('index.html', current_anagrams = Markup(r.replace(",", "<br>")), previous_anagrams = Markup(request.form['previous_anagrams']))

if __name__ == "__main__":
    app.run()
