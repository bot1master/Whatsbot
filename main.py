from data import add_user
from responses import get_response
name = input("ما اسمك؟ ")
add_user(name)
print (f"أهلا {name} 👋")
while True:
    msg = input("أنت: ")
    response = get_response(msg, name)
    if response == "exit":
        print ("البوت: مع السلامة 👋")
        break
    else:
        print ("البوت:", response)
