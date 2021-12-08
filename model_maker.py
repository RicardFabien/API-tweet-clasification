import html

import joblib
import pandas as pa
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC

comments = pa.read_csv("labels.csv")


tweets = comments["tweet"].transform(lambda line: html.unescape(line))

comments.drop('tweet', axis=1, inplace=True)

X = tweets
y = comments[ ["class"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=413)

clf = make_pipeline(
    TfidfVectorizer(stop_words='english'),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf.fit(X_train,y_train)

print(clf.score(X_test,y_test))

joblib.dump(clf,"model.pkl")
