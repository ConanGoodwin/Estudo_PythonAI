from flask import Flask, render_template, request
from database import get_user, list_users

app = Flask(__name__)


@app.route("/")
def index():
    users = list_users()
    return render_template("index.html", users=users)


@app.route("/user/<user_id>")
def user_details(user_id):
    user = get_user(user_id)

    if not user:
        return "Usuário não encontrado", 404

    if request.method == "POST":
        pass

    return render_template("user.html", user=user, user_id=user_id)


if __name__ == "__main__":
    app.run(debug=True)
