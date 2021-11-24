## Instrucciones sin Docker
El siquiente programa contiene dos APIs y una lógica de llenado de base de datos con todas las posibles placas, al ejecutar la app.py se iniciará el proceso de llenado, luego queará disponible el servicio de las APIs

### Api
Las dos Apis están en el archivo app.py, una ves intales las librerías que están en el archivo requirements.txt con el comando *pip install -r requirements.txt*, puedes ejecutar el servicio en consola con *python app.py*

### Test
Una vez esté ejecutandose el servicio podrás probarlo con postman o haciendo uso del archivo test.py, lo editas con la ip requerida, pasas los datos necesarios para la API que desees probar y listo, lo ejecutas en otra terminal con *python test.py", antes de usarlo verifica la BASE, e ingresa bien los datos.

#### DISCUPLPAS & HERRAMIENTAS
el llenado de la base de datos en un mal pc como el mío puede tardar días, puede modificarse el codigo en app.py para luego de correrlo una vez y que se hayan llenado unas cuantas placas, ya no se ejecute de nuevo y corra directo el servicio. Se hizo uso de Flask para las APIs, SQLAlchemy para las conecciones en pipeline, y sqlite3 para la base de datos. Comenta la linea 34 de app.py donde se llama la funcion createDb() si quieres usar la base de datos añadida

#### db
se añadio una base de datos que va hasta la placa ABAO808 cuya posicion es 690808 que sería la máxima, si quieres usar la base de datos agregada usa estos rangos para probar.

#### Hotfix features
- En la base de datos el id corresponde al ID de la placa anterior esto se debe a que falta la placa AAAA000 ya que tenía un error en la linea 70 del archivo filldb.py que quedó comentada.
- Validación añadida a GetPatent
## Instrucciones con Docker
proximamente...