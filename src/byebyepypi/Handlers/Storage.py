from datetime import datetime

class Storage(object):
    request_cache = {}
    
    @classmethod
    def add_to_cache(cls, egg, request):
        cls.request_cache[egg] = {'response': request, 'time': datetime.now()}
        
    @classmethod
    def get_from_cache(cls, egg):
        if cls.request_cache.has_key(egg):
            return cls.request_cache[egg]
        return None