from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<!doctype html>
<html>
    <title>LAPTOP</title>
    <body>
        LAPTOP CONFIGURATION
        <TABLE border="10" celpadding="15">
            <tr><th>SYSTEM CONFIGURATION</th> <th>DESCRIPTION</th></tr>
            <tr><td>Processor</td> <td> Intel core-i5</td></tr>
            <tr><td>Primary Memory</td> <td>16GB Ram</td></tr>
            <tr><td>Secondary Memory</td> <td>512GB ssd</td></tr>
            <tr><td>OS</td> <td>Windows 11</td></tr>
            <tr><td>Graphics Card</td> <td>NVIDIA GeForce MX550</td></tr>
        </TABLE>
    </body>
</html>

'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()