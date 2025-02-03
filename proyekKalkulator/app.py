from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aritmatika", methods=["POST"])
def aritmatika():
    a = int(request.form["a"])
    b = int(request.form["b"])
    n = int(request.form["n"])

    da = []
    for i in range(n):
        da.append(a + (i * b))

    return render_template("hasil_aritmatika.html", da=da)

@app.route("/geometri", methods=["POST"])
def geometri():
    a = int(request.form["a"])
    b = int(request.form["b"])
    n = int(request.form["n"])

    dg = []
    for i in range(n):
        dg.append(a * (b ** i))

    return render_template("hasil_geometri.html", dg=dg)

if __name__ == "__main__":
    app.run(debug=True)
