# Challenge Bigbox | Alexander Graus

## Descripcion:
El ejercicio consiste en mostrar una lista de Boxes junto con sus actividades, utilizando Django y postgres.

### Comentario sobre la descripcion del Box 'Bonjour'

En la BD la descriocion del box viene como html (con el tag p ) entonces en box_list.html y en box_detail.html lo mostre con el filtro safe. 

Pero, solo lo haria si tengo garantizado que es realmente seguro y no un riesgo de [XSS](https://owasp.org/www-community/attacks/xss/) (Cross site scripting) Ejemplo, un usario podria cargar un tag script y ejecutar codigo malicioso.

En estos casos se podria usar https://pypi.org/project/html-sanitizer/