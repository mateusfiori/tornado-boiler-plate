import tornado.web

class HealthController(tornado.web.RequestHandler):
    def get(self):
        self.write('To vivo')