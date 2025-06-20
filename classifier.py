from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def train_classifier(documents, labels):
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(documents, labels)
    joblib.dump(model, 'classifier.joblib')
    return model

def predict_category(model, document):
    return model.predict([document])[0]