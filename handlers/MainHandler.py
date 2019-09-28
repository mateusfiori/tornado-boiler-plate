import tornado.web
from handlers.BaseHandler import BaseHandler

class MainHandler(BaseHandler):
    
    SUPPORTED_METHODS = ['GET']

    def initialize(self, **kwargs):
        self.db = kwargs.get('db')

    def get(self):
        self.send_response({"Hello": "World"})