from flask import Flask,request,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/convert", methods=['POST'])
def translate():
    pass

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
