# Desafío DevOps RockingData

## Estructura de repositorio
```
📂  uploads ➡ Carpeta que contendrá los archivos
      📄 Arg.png
      📄 testOne.txt
      📄 testTwo.txt
📄 app.py ➡ Microservicio con solicitudes GET, POST y DELETE
📄 Dockerfile ➡ Archivo que contiene la imagen base del contenedor y las características  del microservicio python e inicia el script app.py
📄 README.md
📄 run-docker.py ➡ Script python que construye la imagen del microservicio e inicializa el contenedor en el puerto 8000
📄 run-docker.sh ➡ Script que construye la imagen del microservicio e inicializa el contenedor en el puerto 8000 
```

## Instrucciones para levantar el contenedor
- Primero que nada tener instalado docker en su máquina y python si se utiliza el script de python para construir el contenedor e iniciarlo
- Para construir e iniciar el contenedor ejecutar en su terminal: 
```
./run-docker.sh o python3 run-docker.py
```
*Importante* ➡ Para acceder al contenedor puede hacerlo por: localhost:8000/files por ejemplo, es decir el servicio http se levanta en el puerto 8000, ya que está configurado de esta manera.

## Instrucciones para acceder a cada uno de los microservicios

### Obtener o listar archivos
Para obtener la lista de archivos hay dos formas
- Ingresando por el navegador a http://localhost:8000/files
- Utilizando Postman, Thunder Client haciendo una petición get a dicha URL: http://localhost:8000/files
- Haciendo un curl de la siguiente manera: curl http://localhost:8000/files
  
### Subir archivo
- Utiliza una solicitud POST a http://localhost:8000/upload-file
    - Selecciona la pestaña "Body" y elige la opción "binary"
    - Selecciona un archivo utilizando el botón "Select File" y establece el encabezado "File-Name" con el nombre que deseas darle al archivo
- curl -X POST -H "File-Name: example.txt" --data-binary "/file.txt(Reemplazar con la correspondiente ruta)" http://localhost:8000/upload-file

### Eliminar archivo
- Utilizando Postman, Thunder Client haciendo una petición delete a dicha URL: http://localhost:8000/delete-file/example.txt(Reemplazar con el correspondiente nombre del archivo)
- curl -X DELETE http://localhost:8000/delete-file/example.txt

## Repositorio

https://github.com/Frangia22/challengeRockingData
