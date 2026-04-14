# -*- coding: utf-8 -*-

from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai

app = Flask(__name__)

# ✅ API KEY من Render
openai.api_key = os.getenv("OPENAI_API_KEY")

# تخزين حالة المستخدم
user_state = {}

@app.route("/")
def home():
    return "Bot is running"

@app.route("/chat", methods=["POST"])
def chat():
    incoming_msg = request.values.get("Body", "").strip().lower()
    sender = request.values.get("From", "")

    resp = MessagingResponse()
    msg = resp.message()

    # القائمة
    if incoming_msg in ["menu", "hi", "اهلا"]:
        msg.body(
            "اهلا بك\n"
            "1- اختبار\n"
            "2- طلب\n"
            "3- معلومات\n"
            "4- ذكاء"
        )

    elif incoming_msg == "1":
        msg.body("تم الاختبار")

    elif incoming_msg == "2":
        user_state[sender] = "order"
        msg.body("اكتب طلبك")

    elif incoming_msg == "3":
        msg.body("هذا بوت واتساب يعمل بالذكاء")

    elif incoming_msg == "4":
        user_state[sender] = "ai"
        msg.body("اكتب سؤالك")

    # الذكاء الاصطناعي
    elif user_state.get(sender) == "ai":
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": incoming_msg}
                ]
            )
            reply = response.choices[0].message.content
            msg.body(reply)

        except Exception as e:
            print (e)
            msg.body("حدث خطأ في الذكاء")

    # الطلبات
    elif user_state.get(sender) == "order":
        with open("orders.txt", "a") as f:
            f.write(f"{sender}: {incoming_msg}\n")

        user_state[sender] = None
        msg.body("تم تسجيل طلبك")

    else:
        msg.body("اكتب menu")

    return Response(str(resp), mimetype="application/xml")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
