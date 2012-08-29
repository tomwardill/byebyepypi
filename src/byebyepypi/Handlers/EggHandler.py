import tornado.web

class EggHandler(tornado.web.RequestHandler):
    
    def get(self, egg):
        print 'EggHandler: ' + egg
        self.write('foo')