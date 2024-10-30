# my_web_framework/framework/router.py
from http.server import BaseHTTPRequestHandler

class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def get_handler(self):
        router = self

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                handler = router.routes.get(self.path)
                if handler:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    response = handler()
                    self.wfile.write(response.encode("utf-8"))
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"404 Not Found")

        return RequestHandler
