from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    # handle the POST request
    if request.method == 'POST':
        texte = request.form.to_dict(flat=False)
        summary = requests.post("http://max:5000/model/predict", json=texte)
        summary = json.loads(summary.content.decode())
        return '''<h1>Text summary : {}</h1>'''.format(summary['summary_text'][0])

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Your text to summarize is: <input type="text" name="text"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
