from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def helloWorld(): 
    return "Hello World !"

@app.route('/formulaire', methods=['POST', 'GET'])
def formulaire(): 
    texte = None
    if request.method == 'POST': 
        texte = request.form['texte']
    return render_template('formulaire.html', texte=texte)
if __name__=="__main__": 
    app.run(host='0.0.0.0', debug=True)