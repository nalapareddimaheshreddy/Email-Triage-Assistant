from flask import Blueprint, request, jsonify
from services.summarizer import summarize_email
from services.classifier import classify_email
from services.priority import detect_priority
from services.reply_generator import generate_reply

email_routes = Blueprint("email_routes", __name__)

@email_routes.route("/process-email", methods=["POST"])
def process_email():
    data = request.json
    email_text = data.get("email")

    summary = summarize_email(email_text)
    category = classify_email(email_text)
    priority = detect_priority(email_text)
    reply = generate_reply(email_text)

    return jsonify({
        "summary": summary,
        "category": category,
        "priority": priority,
        "reply": reply
    })

