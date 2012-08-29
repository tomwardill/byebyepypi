from datetime import datetime

import tornado.web
import requests

from byebyepypi import settings

class ListHandler(tornado.web.RequestHandler):
    
    response_cache = {}
    
    def get(self, egg):
        print 'EggHandler: ' + egg
        
        if self.response_cache.has_key(egg) and datetime.now() < (self.response_cache[egg]['time'] + settings.CACHE_TIME):
                print 'Returning cache for: ' + egg
                self.write(self.response_cache[egg]['response'])
                return
            
        
        r = requests.get(settings.PYPI_URL + egg)
        if (r.status_code > 200):
            raise tornado.web.HTTPError(r.status_code)
        
        self.response_cache[egg] = {'response': r.text, 'time': datetime.now()}
        
        self.write(r.text)