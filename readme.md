## Instrucciones sin Docker
El siquiente programa contiene dos APIs y una lógica de llenado de base de datos con todas las posibles placas, al ejecutar la app.py se iniciará el proceso de llenado, luego queará disponible el servicio de las APIs

### Api
Las dos Apis están en el archivo app.py, una ves intales las librerías que están en el archivo requirements.txt con el comando *pip install -r requirements.txt*, puedes ejecutar el servicio en consola con *python app.py*

### Test
Una vez esté ejecutandose el servicio podrás probarlo con postman o haciendo uso del archivo test.py, lo editas con la ip requerida, pasas los datos necesarios para la API que desees probar y listo, lo ejecutas en otra terminal con *python test.py", antes de usarlo verifica la BASE, e ingresa bien los datos.

#### DISCUPLPAS & HERRAMIENTAS
el llenado de la base de datos en un mal pc como el mío puede tardar días, puede modificarse el codigo en app.py para luego de correrlo una vez y que se hayan llenado unas cuantas placas, ya no se ejecute de nuevo y corra directo el servicio. Se hizo uso de Flask para las APIs, SQLAlchemy para las conecciones en pipeline, y sqlite3 para la base de datos

## Instrucciones con Docker
proximamente...