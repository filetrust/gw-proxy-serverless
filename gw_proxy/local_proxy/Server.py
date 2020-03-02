import threading
from http.server import HTTPServer

from gw_proxy.local_proxy.Handle_Request import Handle_Request


class Server():
    def __init__(self, port=None, target=None, host=None):
        self.port   = port
        self.host   = host
        self.target = target
        self.scheme = 'http'
        self.httpd  = None


    def setup(self):
        if self.port   is None: self.port   = 7788
        if self.host   is None: self.host   = '127.0.0.1'
        if self.target is None: self.target = 'https://httpbin.org'
        Handle_Request.proxy_target = self.target
        self.httpd = HTTPServer((self.host, self.port), Handle_Request)
        return self

    def start(self):
        self.httpd.serve_forever()

    def start_async(self):
        if self.httpd is None:
            self.setup()
        thread = threading.Thread(target=self.start)
        thread.start()
        return self

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

    def url(self, path=''):
        return f'{self.scheme}://{self.host}:{self.port}/{path}'
        
