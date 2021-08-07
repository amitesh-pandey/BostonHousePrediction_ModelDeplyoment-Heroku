from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

filename = 'final_model.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route("/")
def template():
    return render_template('index.html')

@app.route("/submit", methods = ['GET','POST'])
def predict():
    # html to python file
    if request.method == "POST":
        crim = request.form['crim']
        zn = request.form['zn']
        indus = request.form['indus']
        chas = request.form['chas']
        nox = request.form['nox']
        rm = request.form['rm']
        age = request.form['age']
        dis = request.form['dis']
        rad = request.form['rad']
        tax = request.form['tax']
        ptratio = request.form['ptratio']
        b = request.form['b']
        lstat = request.form['lstat']

        result = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
        prediction = model.predict(result)

    # python file to html
    return render_template("submit.html", n = prediction )


if __name__ == "__main__":
    app.run(debug = True)



