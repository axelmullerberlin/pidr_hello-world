from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/formulaire', methods=['POST'])
def formulaire():
    data=request.json
    texte=data.get('texte', '')
    return jsonify({"message": f"{texte}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)