import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somebody'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    ADMINS = ['hostmail@gmail.com']
    WHOOSH_BASE = os.path.join('proj/','search.db')