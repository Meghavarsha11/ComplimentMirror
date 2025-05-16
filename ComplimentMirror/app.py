from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Load compliments
def load_compliments():
    with open("compliments.txt", "r") as file:
        return [line.strip() for line in file if line.strip()]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compliment")
def get_compliment():
    compliments = load_compliments()
    chosen = random.choice(compliments)
    return jsonify({"compliment": chosen})

@app.route("/submit", methods=["POST"])
def submit_compliment():
    data = request.get_json()
    compliment = data.get("compliment", "").strip()
    if compliment:
        with open("compliments.txt", "a") as file:
            file.write(f"{compliment}\n")
        return jsonify({"status": "success", "message": "Thanks for your compliment!"})
    return jsonify({"status": "error", "message": "Empty compliment"}), 400
@app.route("/compliments/all")
def get_all_compliments():
    compliments = load_compliments()
    return jsonify({"compliments": compliments})

if __name__ == "__main__":
    app.run(debug=True)
