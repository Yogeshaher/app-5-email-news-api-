import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "yaher3335@gmail.com"
    password = "xufiwrbcnevewuvb"

    receiver = "yaher3335@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)