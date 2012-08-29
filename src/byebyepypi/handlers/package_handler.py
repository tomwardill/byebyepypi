import logging

import tornado.web
import requests

from byebyepypi import settings

class PackageHandler(tornado.web.RequestHandler):
    """Handle package download and cache
    """
    
    def get(self, category, package_name, package_file):
        logging.info(category)
        logging.info(package_name)
        logging.info(package_file)
        
        f = requests.get(settings.PYPI_URL + self.request.uri)
        logging.info(len(f.content))
        self.set_header('Content-Disposition', 'attachment; filename=' + package_file)
        self.set_header('Content-Type', 'application/x-tar')
        self.write(f.content)