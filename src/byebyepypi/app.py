import logging

import tornado.web
import simplejson as json
from byebyepypi.Handlers import IndexHandler

def run(host, port):
    """ Run the server until killed
    """
    
    application = tornado.web.Application([
        (r'/', IndexHandler),
        ])
    application.listen(port=port, address=host)
    tornado.ioloop.IOLoop.instance().start()