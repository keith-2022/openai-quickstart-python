import os

import openai
from flask import Flask, redirect, render_template, request, url_for,jsonify

app = Flask(__name__)
## openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(question),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

# Define greet rounte and its methods
@app.route("/greet")
def greet():
    question = request.args["question"]
    answer = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(question),
        temperature=0.6,
    )
    response = {"question": f"{question}", "answer": f"{answer.choices[0].text}"}
    return jsonify(response)

@app.route("/error")
def error():
    return jsonify({"status":"error"})

def generate_prompt(animal):
    return """{}""".format(
        animal.capitalize()
    )

