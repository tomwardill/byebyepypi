import tornado.web

from storage import Storage

class CacheHandler(tornado.web.RequestHandler):
    """ View and clear the cache
    """
    
    def get(self, mode):
        
        if mode == 'clear':
            Storage.clear_cache()
            self.write('cleared')
        else:
            self.write('unknown mode')
            