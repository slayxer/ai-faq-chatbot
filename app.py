from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
data = pd.read_csv("dataset.csv")

questions = data["question"]
answers = data["answer"]

# Convert questions to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_input = request.json["message"]

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, X)

    index = similarity.argmax()

    response = answers[index]

    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)