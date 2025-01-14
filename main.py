import eel

eel.init("public")

eel.start("home.html")

@eel.expose

def send_data():
    return eel.send_data("hello")