import logging

import tornado.web

class PackageHandler(tornado.web.RequestHandler):
    """Handle package download and cache
    """
    
    def get(self, category, package_name, package_file):
        logging.info(category)
        logging.info(package_name)
        logging.info(package_file)