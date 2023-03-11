import os

import openai
from flask import Flask, redirect, render_template, request, url_for

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


def generate_prompt(animal):
    return """{}""".format(
        animal.capitalize()
    )
