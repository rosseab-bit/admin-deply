# admin-deploy

Esta api esta creada para despliegue de contenedores docker, la misma esta protegida mediante acceso con tokens - jwt. Este login lo hacemos mediante el microservicio [login-api-nodejs](https://github.com/rosseab-bit/login-api-nodejs) que se encuentra dentro de mi cuenta de [GitHub](https://github.com/rosseab-bit)

## Path packages
En esta carpeta tenemos modulos de apoyo al codigo principal 

## Rutas 
Dentro de esta carpeta encontraremos el archivo index con todas las rutas
* /api/dockerbuild : En esta ruta podremos desplegar nuevos contenedores. Tenemos que pasar 
la imagen de docker donde queremos desplegar, el nombre del repo de github a demas del token para poder hacer la operacion. Este token lo tenemos de una api de login que lo pueden encontrar en mi cuenta [login-api-nodejs](https://github.com/rosseab-bit/login-api-nodejs).
```json
{
	"docker_image": "python:3.9.13-alpine3.15",
	"github_repo": "miapp3",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjY3NTEzNjk4fQ.c-YcIVayHp6kUEHi2UzwV1Lg7Tts1fz2xsPM2Z-EVVI"
}
```
* /api/pullbranch: En esta ruta podremos actualizar una rama especifica de un repo y volver a
correr el contenedor. 
```json
{
	"branch": "develop",
	"github_repo": "miapp3",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjY3NTEzNjk4fQ.c-YcIVayHp6kUEHi2UzwV1Lg7Tts1fz2xsPM2Z-EVVI"
}
```
* /api/listapp: En esta ruta tendremos una lista de las apps corriendo en el server y el path donde se encuentran.
```json
{
	"apps_list": [
		"miapp4",
		"miapp1",
		"miapp2",
		"miapp3",
		"miapp5"
	],
	"path": "docker_deploys"
}
```

##Contacto
[LinkedIn](https://www.linkedin.com/in/roseabdev/)
