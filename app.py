from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

app = Flask(__name__)

# Load the pre-trained model and TF-IDF vectorizer
model_tfidf = joblib.load("model_tfidf.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Function to perform text preprocessing
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if (word.isalpha() and word not in stop_words)]
    stemmer = SnowballStemmer("english")
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['text']
        preprocessed_text = preprocess_text(input_text)
        input_tfidf = tfidf_vectorizer.transform([preprocessed_text])
        prediction = model_tfidf.predict(input_tfidf)[0]
        return render_template('index.html', prediction=prediction, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True , use_reloader=False)
