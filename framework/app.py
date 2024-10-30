from http.server import BaseHTTPRequestHandler, HTTPServer
from .router import Router

class App:
    def __init__(self):
        self.router = Router()

    def route(self, path):
        def wrapper(handler):
            self.router.add_route(path, handler)
            return handler
        return wrapper

    def start(self, host="localhost", port=8000):
        server = HTTPServer((host, port), self.router.get_handler())
        print(f"Server running on http://{host}:{port}")
        server.serve_forever()
