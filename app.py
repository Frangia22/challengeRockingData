import http.server
import socketserver
import os 
import json 

upload_file = './uploads'

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload-file':
            content_length = int(self.headers['Content-Length'])
            file_data = self.rfile.read(content_length)
            file_name = self.headers['File-Name']
            file_path = os.path.join(upload_file, file_name)

            with open(file_path, 'wb') as f:
                f.write(file_data)

            self.send_response(200)
            self.end_headers()
            response = {'message': 'Archivo subido con exito!!'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {'error': 'Ruta no encontrada'}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def do_GET(self):
        if self.path == '/files':
            files = os.listdir(upload_file)
            self.send_response(200)
            self.end_headers()
            response = {'files': files}
            self.wfile.write(json.dumps(response, indent=4).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {'error': 'Ruta no encontrada'}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def do_DELETE(self):
        if self.path.startswith('/delete-file/'):
            filename = self.path[len('/delete-file/'):]

            file_path = os.path.join(upload_file, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                self.send_response(200)
                self.end_headers()
                response = {'message': 'Archivo eliminado con exito'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                response = {'error': 'Archivo no encontrado'}
                self.send_response(404, response)
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {'error': 'Ruta no encontrada'}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))


if __name__ == '__main__':
    if not os.path.exists(upload_file):
        os.makedirs(upload_file)

    PORT = 8000
    Handler = CustomRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()