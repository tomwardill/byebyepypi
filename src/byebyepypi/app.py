import logging

import tornado.web
import tornado.options
import simplejson as json
from byebyepypi.handlers import IndexHandler, DebugHandler, ListHandler, CacheHandler, PackageHandler

def run(host, port):
    """ Run the server until killed
    """
    
    application = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/index/([A-z0-9\.]+)[/]?', ListHandler),
        (r'/cache/([A-z0-9]+)[/]?', CacheHandler),
        #/packages/source/z/zc.recipe.egg/zc.recipe.egg-1.3.2.tar.gz
        (r'/packages/source/([A-z0-9]+)/([A-z0-9\.]+)/([A-z0-9\.-]+)', PackageHandler),
        (r'.*', DebugHandler),
        ])
    tornado.options.parse_command_line()
    application.listen(port=port, address=host)
    tornado.ioloop.IOLoop.instance().start()