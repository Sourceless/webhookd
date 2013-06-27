try:
    import BaseHTTPServer as h
except ImportError:
    import http.server as h

class WebhookHandlerFactory(object):
    def __init__(self, callback):
        return RequestHandler

    class RequestHandler(h.BaseHTTPRequestHandler):
        server_version = 'webhookd/1.0'
        def do_all(self):


        def do_GET(self):
            do_all()

        def do_POST(self):
            do_all()

        def do_PUT(self):
            do_all()

        def do_
            


address = ('', 80)
httpd = h.HTTPServer

if __name__ == '__main__':
    httpd.serve_forever()
