flaskinstall = True
while flaskinstall:
    try:
        from flask import Flask, redirect, url_for, render_template, request, session
        flaskinstall = False
    except ModuleNotFoundError:
        import os
        os.system('cmd /c "pip install flask"')

#   This is just initializing flask
app = Flask(__name__)
app.secret_key = "Hello"

showhowold = "True"

#   Decorating the site
@app.route("/")
def home():
    #   Returns the rendered web-page i.e. front end html code
    #return render_template("index.html", isUser = "Hi ", name_="Stranger!", namesList = ["Tanvir", "Toha", "Tanzil", "Mehedi"])
    return redirect(url_for("login"))


@app.route("/<name>")
def homepage(name):
    global showhowold
    if name == "Home":
        return render_template("index.html", isUser = "Hi, ", name = "Stranger!", showhowold = "False")
    elif name == "home":
        return render_template("index.html", isUser = "Hi ", name = "Stranger!", showhowold = "False")
    else:
        if "user" in session:
            return render_template("index.html", isUser = "Hi ", name = name, showhowold = "False")
        return redirect(url_for("login"))


@app.route("/login", methods = ["POST", "GET"])
def login():
    #   Example of using GET and POST
    if "user" in session:
        return redirect(url_for("user"))
    else:
        if request.method == "POST":
            session["user"] = request.form["nm"]
            session["age"] = request.form["age"]
            return redirect(url_for("user"))
        else:
            return render_template("login.html")



@app.route("/user")
def user():
    global showhowold
    if "user" in session:
        name = session["user"]
        age = session["age"]
        return render_template("index.html",isUser = "Your name is " , name = name, age = age, showhowold = "True")
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("age", None)
    return redirect(url_for("login"))

#   To make sure the code only works if it is run from within itself (whatever that means)
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")