import tornado.web
import requests

from byebyepypi import settings

class ListHandler(tornado.web.RequestHandler):
    
    def get(self, egg):
        print 'EggHandler: ' + egg
        
        r = requests.get(settings.PYPI_URL + egg)
        if (r.status_code > 200):
            raise tornado.web.HTTPError(r.status_code)
        
        self.write(r.text)