from flask import Flask, request, render_template
import os, csv

app = Flask(__name__)

dictionary = {key: value for key, value in csv.reader(open("dictionary"))}

@app.route('/', methods=['GET', 'POST'])
def unscrambleWord():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		try:
			inputAnagrams = dictionary[''.join(sorted(''.join([i for i in request.form['inputAnagrams'].lower() if i.isalpha()])))]
		except KeyError:
			return render_template('index.html', anagrams = request.form['previousAnagrams'], static = True)
		if request.form['previousAnagrams'] == '':
			return render_template('index.html', anagrams = inputAnagrams.replace(',', ', '), static = False)
		return render_template('index.html', anagrams = inputAnagrams.replace(',', ', ') + "<hr>" + request.form['previousAnagrams'], static = False)

if __name__ == "__main__":
	app.run()
