from flask import Flask, request, jsonify
from solo import run_solo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")

    response = run_solo(query)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()