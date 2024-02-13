from http.server import BaseHTTPRequestHandler, HTTPServer
import re

from form_urlencoded import get_POST_data


class Router(BaseHTTPRequestHandler):
    routes = {"GET": {}, "POST": {}, "DELETE": {}}

    def add_route(method, path_pattern, callback):
        method_routes = Router.routes[method]
        method_routes[path_pattern] = callback

    def do_POST(self):
        routes = Router.routes["POST"]
        route = self._match_route(routes)
        if not route:
            self._respond(405, "Method Not Allowed")
            return
        callback = route["callback"]
        param = route["param"]
        form_data = get_POST_data(self)
        context = {"param": param, "form_data": form_data}
        body = callback(context)
        self._respond(200, body)

    # Repeated for do_GET, do_DELETE, etc.

    def _match_route(self, routes):
        for route_pattern in routes.keys():
            match = re.fullmatch(route_pattern, self.path)
            if match:
                route_param = match.group(1) if match.groups() else None
                route_callback = routes[route_pattern]
                route = {"callback": route_callback, "param": route_param}
                return route

    def _respond(self, code, body):
        self.send_response(code)
        self.end_headers()
        body = body + "\n"
        self.wfile.write(body.encode())


def start(port=8080):
    address = ("localhost", port)
    server = HTTPServer(address, Router)
    print(
        f"Server listening at http://{address[0]}:{address[1]} ...\n"
        "Press CTRL + C to stop."
    )
    server.serve_forever()
