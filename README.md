# Desafío DevOps RockingData

## Estructura de repositorio
```
📂  uploads ➡ Carpeta que contiene los archivos existentes y que sean subidos
      📄 testOne.txt
📄 app.py ➡ Microservicio con solicitudes GET, POST y DELETE
📄 README.md
```
## Instrucciones para acceder a cada uno de los microservicios

### Obtener o listar archivos
Para obtener la lista de archivos hay dos formas
- Ingresando por el navegador a http://localhost:5000/list
- Utilizando Postman, Thunder Client haciendo una petición get a dicha URL: http://localhost:5000/list
- Haciendo un curl de la siguiente manera: curl http://localhost:5000/list

### Subir archivo
- Utiliza una solicitud POST a http://localhost:5000/upload
    - Selecciona la pestaña "Body" y elige la opción "binary"
    - Selecciona un archivo utilizando el botón "Select File" y establece el encabezado "X-File-Name" con el nombre que deseas darle al archivo

### Eliminar archivo
- Utilizando Postman, Thunder Client haciendo una petición delete a dicha URL: http://localhost:5000/delete/example.txt
