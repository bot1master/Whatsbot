from data import save_order
step = "menu"
def get_response(msg, name):
    global step
    msg = msg.lower()
    if msg == "خروج":
        return "exit"
    if step == "menu":
        if msg == "menu":
            return "📋 القائمة:\n1- السعر\n2- طلب\n3- معلومات"
        elif msg == "1":
            return "💰 السعر 10$"
        elif msg == "2":
            step = "order"
            return "✍️ اكتب طلبك"
        elif msg == "3":
            return "🤖 بوت متعدد المستخدمين"
        else:
            return "اكتب menu"
    elif step == "order":
        save_order(name, msg)
        step = "menu"
        return "✅ تم حفظ طلبك"
