import logging

import tornado.web
import tornado.options
import simplejson as json
from byebyepypi.handlers import IndexHandler, DebugHandler, ListHandler, CacheHandler

def run(host, port):
    """ Run the server until killed
    """
    
    application = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/index/([A-z0-9\.]+)[/]?', ListHandler),
        (r'/cache/([A-z0-9]+)[/]?', CacheHandler),
        (r'.*', DebugHandler),
        ])
    tornado.options.parse_command_line()
    application.listen(port=port, address=host)
    tornado.ioloop.IOLoop.instance().start()