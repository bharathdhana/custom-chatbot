from flask import Flask, request, render_template, jsonify
from chatbot import get_response
from database import save_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.json.get("msg")
    bot_response = get_response(user_input)
    save_message(user_input, bot_response)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
