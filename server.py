from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = "YABBADABBADOO!"

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def process():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    if comment == "":
        comment = "None"
    if not len(name):
        flash("Name field cannot be empty")
        return redirect("/")
    elif len(comment) > 120:
        flash("Comment field cannot be more than 120 characters")
        return redirect("/")
    return render_template("result.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True)