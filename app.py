import http.server #Modulo para manejar solicitudes http
import socketserver # Modulo para exponer el microservicio
import os #Modulo con funcionalidades dependientes del SO
import json #Permite trabajar con archivos y cadenas de caracteres JSON

upload_file = './uploads'

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            file_data = self.rfile.read(content_length)
            file_name = self.headers['X-File-Name']
            file_path = os.path.join(upload_file, file_name)

            with open(file_path, 'wb') as f:
                f.write(file_data)

            self.send_response(200)
            self.end_headers()
            response = {'message': 'Archivo subido con exito!!'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            response = {'message': 'Lo siento hubo un error'}
            self.send_error(404, response)

    def do_GET(self):
        if self.path == '/list':
            files = os.listdir(upload_file)
            self.send_response(200)
            self.end_headers()
            response = {'files': files}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            super().do_GET()

    def do_DELETE(self):
        if self.path.startswith('/delete/'):
            filename = self.path[len('/delete/'):]

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
            response = {'message': 'Lo siento hubo un error'}
            self.send_error(404, response)


if __name__ == '__main__':
    if not os.path.exists(upload_file):
        os.makedirs(upload_file)

    PORT = 5000
    Handler = CustomRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()