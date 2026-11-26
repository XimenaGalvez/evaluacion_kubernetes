from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(mensaje="Hola, soy Ximena Hernández", hora_servidor=hora)

@app.route('/healthz')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
