#!/bin/python3

################################################################################
# A Python script to open a http(1.1) server INSECURELY for file transfer in LAN
################################################################################

import socket, http.server, socketserver, sys, os

try:
    if os.name == 'posix' :
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("0.0.0.254", 80))
        ip_address=s.getsockname()[0]
    else :
        ip_address = socket.gethostbyname(socket.gethostname())
except:
    ip_address = "local"

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Current Directory at: {ip_address}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\033[3D\x1b[2K--EXITED--")
        httpd.server_close()
        sys.exit(0)
