from threading import Thread
from flask_mail import Message
from app import app, mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_text(email, text):
    send_email('Your result',
               sender=app.config['ADMINS'][0],
               recipients=email,
               text_body=text)