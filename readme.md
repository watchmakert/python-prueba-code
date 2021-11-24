## Instrucciones sin Docker
El siquiente programa contiene dos APIs conectadas a unas funciones que con operaciones matemáticas dada una placa con formato XXXX### se dará un id o posicion en lista(si las contaramos) o te dará la placa si le das la posicion o id

### Api
Las dos Apis están en el archivo app.py, una ves instales las librerías que están en el archivo requirements.txt con el comando *pip install -r requirements.txt*, puedes ejecutar el servicio en consola con *python app.py*

### Test
Una vez esté ejecutandose el servicio podrás probarlo con postman o haciendo uso del archivo test.py que se encuentra en la misma carpeta, lo editas con la ip requerida, pasas los datos necesarios para la API que desees probar y listo, lo ejecutas en otra terminal con *python test.py".

### Tener en cuenta
Las placas las conté creciendo de derecha a izquierda lo que quiere decir que luego de la placa AAAA999 la letra que aumentará será la primera a la izquiera, siendo la siguiente placa la siguiente AAAB000 y así suscesivamente. 

#### Soluciones
La info anterior es respecto a la solucion principal, la solucion matemática, sin embargo, existe otra solucion, una con base de datos y por fuerza bruta, si bien no es optima, muestra conocimientos en bases de datos adicionales.

## Instrucciones con Docker
proximamente...