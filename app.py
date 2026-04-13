from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
user_state = {}
@app.route("/")
def home():
    return "WhatsApp Bot is running ✅"
@app.route("/chat", methods=["POST"])
def chat():
    incoming_msg = request.values.get('Body', '').strip()
    sender = request.values.get('From', '')
    resp = MessagingResponse()
    msg = resp.message()
    if incoming_msg.lower() == "menu":
        user_state[sender] = None
        msg.body("📋 القائمة:\n1- السعر\n2- طلب\n3- معلومات")
    elif incoming_msg == "1":
        msg.body("💰 السعر: 10$")
    elif incoming_msg == "2":
        user_state[sender] = "waiting_order"
        msg.body("✍️ اكتب طلبك الآن")
    elif incoming_msg == "3":
        msg.body("ℹ️ نحن نقدم خدمات برمجة وتصميم")
    elif user_state.get(sender) == "waiting_order":
        with open("orders.txt", "a") as f:
            f.write(f"{sender}: {incoming_msg}\n")
        user_state[sender] = None
        msg.body("✅ تم حفظ طلبك بنجاح")
    else:
        msg.body("❌ لم أفهم، اكتب menu")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
