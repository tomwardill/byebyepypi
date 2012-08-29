import tornado.web

class DebugHandler(tornado.web.RequestHandler):
    
    def get(self):
        print 'debug - get: ' + self.request.uri
    
    def post(self):
        print 'debug - post: ' + self.request.uri