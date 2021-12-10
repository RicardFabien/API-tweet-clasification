import joblib
from flask import Flask, request, render_template
import os

model = joblib.load("model.pkl")

classification = {0: "Contenue haineux", 1: "Language offensant", 2: "Contenue benin"}

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    tweet_type = -1
    text = ""
    if request.method == 'POST':
        text = request.form.get('txt')
        tweet_type = classification[get_type(text)]
    return render_template("home.html",txt = text , type=tweet_type)


def get_type(sentence):
    prediction = model.predict([sentence])
    print(prediction)
    return prediction[0]

