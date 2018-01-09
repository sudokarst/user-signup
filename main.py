"""
The user leaves any of the following fields empty: username, password, verify password.
The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
The user's password and password-confirmation do not match.
The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
"""
from flask import Flask, redirect, request, render_template

username = ""

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def validate():
    global username
    validated = True
    username = request.form["username"].strip() # remove whitespace
    username_invalid = "username "
    if not (3 <= len(username) <= 20):
        username_invalid += " must be 3-20 characters long"
        validated = False
    elif ' ' in username:
        username_invalid += " cannot contain spaces"
        validated = False
    else:
        username_invalid = ""
    
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    if validated:
        return redirect("/welcome")
    else:
        return render_template("index.html", **locals())

@app.route("/welcome")
def welcome():
    return render_template("welcome.html", username=username)

if __name__ == "__main__":
    app.run()