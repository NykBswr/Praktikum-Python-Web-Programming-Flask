from flask import Flask, render_template, redirect, url_for, request
import math

app = Flask(__name__, template_folder='template')

#Name
@app.route("/success/<name>")
def success(name):
    return "Welcome %s" % name

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name = user))
    else:
        user = request.args.form["nm"]
        return redirect(url_for("success", name = user))

#Home
@app.route("/Home/")
@app.route("/")
def home():
    return render_template('index.html')

#CV
@app.route("/Curriculum Vitae/")
def CV():
    return render_template('CV.html')

#Sqrt
@app.route("/Square Root/", methods = ["POST","GET"])
def sqrt():
    result=''
    if request.method == 'POST' and 'number' in request.form:
        number=float(request.form.get('number'))
        result = round(math.sqrt(int(number)),2)
    return render_template('sqrt.html', number=number, result=result)

#Debug
if __name__=="__main__":
    app.run(debug=True)
