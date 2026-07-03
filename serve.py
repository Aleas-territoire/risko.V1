#!/usr/bin/env python3
"""Serveur de test threadé - gère les requêtes en parallèle (contrairement à
python -m http.server qui est mono-thread et peut perdre des tuiles sous charge)."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    server = ThreadingHTTPServer(("", PORT), Handler)
    print(f"Serveur threadé sur http://localhost:{PORT}/")
    server.serve_forever()
