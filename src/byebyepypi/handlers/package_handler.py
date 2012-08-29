import logging

import tornado.web
import requests

from byebyepypi import settings

class PackageHandler(tornado.web.RequestHandler):
    """Handle package download and cache
    """
    
    def get(self, category, package_name, package_file):
        
        f = requests.get(settings.PYPI_URL + self.request.uri)
        self.set_header('Content-Disposition', 'attachment; filename=' + package_file)
        self.set_header('Content-Type', 'application/x-tar')
        self.write(f.content)