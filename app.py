import os
from openai import OpenAI
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request, render_template


load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('404.html')


@app.route("/convert", methods=['POST'])
def translate():
    if request.method == "POST":

        target_code = request.form.get("target_code")
        translate_languagae = request.form.get("translate_language")

        current_code = request.form.get("current_code")
        userinput_code = request.form.get("userinput_code")
        methods = request.form.get("methods")

        prompt = f"\"Translate the user variables into {translate_languagae}; {methods} my {current_code} snippet into a {target_code} code full code ### {current_code} \n\n {userinput_code} \n\n  ### {target_code}"

        completion = client.chat.completions.create(
            model='gpt-3.5-turbo-1106',
            messages=[
                {'role': 'user', 'content': prompt}
            ],
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )
        output = completion.choices[0].message.content
        return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
