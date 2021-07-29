from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    # handle the POST request
    if request.method == 'POST':
        texte = request.form
        summary = requests.post("max:5000", data=texte)
        return '''<h1>Text summary : {}</h1>'''.format(summary.get("summary_text"))

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Your text is: <input type="text" name="texte"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
