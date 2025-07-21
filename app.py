from flask import Flask, request, jsonify
from leave_service import apply_leave, leave_status
from db import get_db
from flask import render_template

app = Flask(__name__)
db = get_db()
collec = db["rule_base"]

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/ask', methods=['POST'])
def chatbot_reply():
    data = request.json
    user_input = data.get("message", "").lower()

    for doc in collec.find():
        for keyword in doc["keywords"]:
            if keyword in user_input:
                return jsonify({"response": doc["responses"][0]})

    return jsonify({"response": "Sorry, I didn't understand that. Try again!"})


@app.route('/apply-leave', methods=['POST'])
def leave_apply_route():
    data = request.json
    regno = data.get("regno")
    name = data.get("name")
    leave_date = data.get("leave_date")
    reason = data.get("reason")

    result = apply_leave(regno, name, leave_date, reason)
    return jsonify({"message": result})


@app.route('/leave-status/<regno>', methods=['GET'])
def leave_status_route(regno):
    result = leave_status(regno)
    return jsonify([{
        "regno": r["regno"],
        "name": r["name"],
        "leave_date": r["leave_date"],
        "reason": r["reason"],
        "status": r["status"]
    } for r in result])


if __name__ == '__main__':
    app.run(debug=True)
