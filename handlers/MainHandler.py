import tornado.web

class MainHandler(tornado.web.RequestHandler):
    
    def initialize(self, **kwargs):
        self.db = kwargs.get('db')

    def get(self):
        self.write("Hello, world")