import smtplib, ssl

host = "smtp.gmail.com"
port = 465



username  = "kraztivan2945@gmail.com"
password = "evgfbawuwdztccza"

receiver = "kraztivan2945@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: TEST, TEST, TEST...
Hi!
How are you??
Bye!

"""
with smtplib.SMTP_SSL(host, port, context= context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)



