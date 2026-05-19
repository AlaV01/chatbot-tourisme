from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": "You are a tourism assistant. Answer clearly and in max 5 lines. Question: " + user_message,
                "stream": False
            }
        )

        data = response.json()
        reply = data["response"]

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Error connecting to AI model."})

if __name__ == "__main__":
    app.run(debug=True)