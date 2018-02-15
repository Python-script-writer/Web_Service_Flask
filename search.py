import fileinput
import sys
import time
from app.email import send_text
from app import db, app


def remove_line(filename):
    for line_number, line in enumerate(fileinput.input(filename, inplace=1)):
        if line_number == 0:
            continue
        else:
            sys.stdout.write(line)


class Post(db.Model):
    __searchable__ = ['body']
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return self.body


def finder_data(text):
    return Post.query.whoosh_search(text).all()


def start():
    while True:
        try:
            with open("text.txt", "r") as data_start:
                data_purse = data_start.readline().split("\n")[0]
                email = data_purse.split("{")[1].split("};")[0].split("'")[1]
                text = data_purse.split("{")[1].split("};")[0].split("'")[3]

            send_text(email, finder_data(text))
            remove_line('text.txt')
        except:
            time.sleep(10)


start()