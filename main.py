"""
Requirements:

Error on

The user leaves any of the following fields empty: username, password, verify password.
The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
The user's password and password-confirmation do not match.
The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.

For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.
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

    #
    # username validation
    #
    username = request.form["username"].strip() # remove whitespace
    username_invalid = "username "
    if not (3 <= len(username) <= 20):
        username_invalid += "must be 3-20 characters long "
        validated = False
    if ' ' in username:
        username_invalid += "cannot contain spaces "
        validated = False
    if username_invalid == "username ":
        username_invalid = ""
    
    #
    # password validation
    #
    password = request.form["password"]
    password2 = request.form["password2"]
    password_invalid = "password "
    if not (3 <= len(password) <= 20):
        password_invalid += "must be 3-20 characters long "
        validated = False
    if ' ' in password:
        password_invalid += "cannot contain spaces "
        validated = False
    if password != password2:
        password2_invalid = "passwords must match! "
        validated = False
    if password_invalid == "password ":
        password_invalid = ""



    #
    # email validation
    #
    email = request.form["email"].strip()
    if email:
        email_invalid = "email "
        email_validated = True
        if not (3 <= len(email) <= 20):
            email_invalid += "must be 3-20 characters long "
            validated = False
        if ' ' in email:
            email_invalid += "cannot contain spaces "
            validated = False
        # one each:
        for good_char in ['@', '.']:
            if email.count(good_char) > 1:
                email_invalid += "cannot contain more than 1 {} ".format(good_char)
                validated = False
            elif email.count(good_char) < 1:
                email_invalid += "must contain 1 {} ".format(good_char)
                validated = False
        if email_invalid == "email ":
            email_invalid = ""

    #
    # git 'er done
    #
    if validated:
        return redirect("/welcome")
    else:
        return render_template("index.html", username=username, **locals())

@app.route("/welcome")
def welcome():
    return render_template("welcome.html", username=username)

if __name__ == "__main__":
    app.run()