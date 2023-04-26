import os
import http.server
import socketserver
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(float(celsius))
    else:
        fahrenheit = ""
    msg = """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>""" + "Fahrenheit: " + str(fahrenheit)
    return msg

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = celsius * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return fahrenheit

port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), http.server.SimpleHTTPRequestHandler)
app.run(host='0.0.0.0', port=port, debug=False)
