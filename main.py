import joblib
import flask

model = joblib.load("model.pkl")

classification = {0 : "Contenue haineux",1: "Language offensant",2 : "Contenue benin"}