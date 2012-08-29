from datetime import datetime

import tornado.web
import requests

from byebyepypi import settings
from Storage import Storage

class ListHandler(tornado.web.RequestHandler):
    
    
    def get(self, egg):
        print 'EggHandler: ' + egg
        
        if Storage.get_from_cache(egg) and datetime.now() < (Storage.get_from_cache(egg)['time'] + settings.CACHE_TIME):
                print 'Returning cache for: ' + egg
                self.write(Storage.get_from_cache(egg)['response'])
                return
            
        
        r = requests.get(settings.PYPI_URL + egg)
        if (r.status_code > 200):
            raise tornado.web.HTTPError(r.status_code)
        
        Storage.add_to_cache(egg, r.text)
        
        self.write(r.text)