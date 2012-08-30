import logging
import os

import tornado.web
import requests

from byebyepypi import settings

class PackageHandler(tornado.web.RequestHandler):
    """Handle package download and cache
    """
    
    def get(self, category, package_name, package_file):
        
        if not os.path.exists(settings.FILE_DIR):
            os.mkdir(settings.FILE_DIR)
            
        if os.path.exists(os.path.join(settings.FILE_DIR, package_file)):
            logging.info('Cached file found')
            cache = open(os.path.join(settings.FILE_DIR, package_file), 'rb')
            self.set_header('Content-Disposition', 'attachment; filename=' + package_file)
            self.set_header('Content-Type', 'application/x-tar')            
            self.write(cache.read())
            return
        
        f = requests.get(settings.PYPI_URL + self.request.uri)
        self.set_header('Content-Disposition', 'attachment; filename=' + package_file)
        self.set_header('Content-Type', 'application/x-tar')
        
        # save the file to cache
        cache = open(os.path.join(settings.FILE_DIR, package_file), 'wb')
        cache.write(f.content)
        cache.close()
        
        self.write(f.content)