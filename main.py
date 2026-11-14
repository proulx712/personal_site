"""Fallback handler. All real pages are static files (see app.yaml)."""


def app(environ, start_response):
    start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
    return [b"Not found"]
