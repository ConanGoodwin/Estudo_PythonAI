from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html", nome="Aluno")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/feedback", methods=["POST"])
def feedback():
    feedback_text = request.form["feedback"]

    return f"Obrigado pelo seu Feedback: {feedback_text}"


if __name__ == "__main__":
    app.run(debug=True)
