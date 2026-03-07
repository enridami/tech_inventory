# Tech Inventory System
#### Video Demo <URL HERE>
#### Description:

## Descripción General

Sistema de Gestión Tecnológico es una app de gestión de inventario basada en línea de comandos desarrollada en Python. Permite a los usuarios poder gestionar un inventario de productos añadiendo, visualizando, editando y eliminando productos mediante una interfaz de menú interactiva (CRUD). La aplicación esta configurada para que los datos se guarden en un archivo CSV, que garantiza la conservación del inventario entre sesiones. El proyecto se desarrollo como proyecto final para CS50P y abarca conceptos fundamentales del lenguaje, como la entrada/salida de archivos, estructura de datos, validación de entradas y pruebas unitarias.

## Estructura del Proyecto
```
project/
├── project.py        # Archivo principal
├── test_project.py   # Tests con pytest
├── requirements.txt  # Dependencias
└── inventory.csv     # Se genera automáticamente
```

## Uso

Al ejecutar el programa aparece el siguiente menú:
```
╔════════════════════════════════════════╗
║       🛒  TECH INVENTORY SYSTEM        ║
╠════════════════════════════════════════╣
║  1. Show products                      ║
║  2. Add product                        ║
║  3. Edit product                       ║
║  4. Delete product                     ║
║  5. Exit                               ║
╚════════════════════════════════════════╝
```
## Archivos del Proyecto

### `project.py`

Es el archivo principal del proyecto, contiene toda la lógica de la app. Dentro de él se encuentran las distintas funciones que estructuran al proyecto, cada una responsable de una tarea en específico.

El archivo comienza con la función `show_menu()`, que muestra el menú de navegación principal por medio de caracteres ASCII. Esto le da a la aplicación una apariencia distinta a solo una linea de comandos en consola, sin depender de bibliotecas externas y manteniendo el proyecto simple.

La función `load_csv()` se encarga de leer los datos de inventario del archivo `inventory.csv` al inicio del programa. Este utiliza la función `csv.DictReader` para analizar cada fila en un diccionario y añadirla a una lista. Cada valor esta validado para que se convierta a su tipo de dato correcto: `id` y `amount` se convierten a `int`, y `price` a `float`. Tuve que convertir los valores porque CSV guarda todo como texto, sin esto, comparar IDs o realizar cálculos con precios no funcionaría. Si el archivo aún no existe (por ejemplo, en la primera ejecución), se captura un error `FileNotFoundError` sin que se detecte y se devuelve una lista vacía.

La función `save_csv()` escribe el estado actual de la lista de inventario en el archivo CSV. Utiliza `csv.DictWriter` con nombres de campo explícitos para garantizar que el orden de las columnas sea siempre coherente y consistente. El parámetro `newline=""` se pasa a `open()` para evitar que aparezcan líneas en blanco adicionales en el archivo en la consola.

La función `show_products()` muestra el inventario en una tabla ASCII de tamaño dinámico, gracias a la lógica implementada. Al principio me encontré con la complejidad de los anchos de columnas de la tabla. En lugar de usar anchos de columna fijos, calcule la longitud máxima de cada campo con `max()` para todos los productos y ajuste el ancho de columna según correspondia. Esto garantizo que la tabla siempre se vea correcta, independientemente de la longitud de los nombres o valores de los productos. El ancho mínimo de cada columna también se compara con la longitud del encabezado de columna, de modo que los encabezados nunca desborden sus columnas en caso de que la longitud del valor sea menor al encabezado.

La función `add_products()` añade un nuevo producto a la lista de inventario. Genera automáticamente un ID único al encontrar el ID máximo existente y sumar 1. Este método es más fiable que usar `len(inventory) + 1`, ya que sigue funcionando correctamente incluso después de eliminar productos.

La función `update()` permite al usuario modificar cualquier campo de un producto existente por su ID. Primero busca el producto en la lista y, si lo encuentra, entra en un bucle interactivo donde el usuario puede elegir qué campo editar. Dado que los diccionarios de Python se pasan por referencia, modificar directamente el producto encontrado también lo actualiza dentro de la lista de inventario.

La función `delete()` elimina un producto por su ID mediante una comprensión de lista. Devuelve una nueva lista que contiene todos los productos excepto el que tiene el ID correspondiente.

Las funciones `get_int()` y `get_float()` son utilidades auxiliares que solicitan repetidamente al usuario la entrada hasta que se introduce un entero o un punto flotante válido. Encapsulan la conversión dentro de un bloque `try/except ValueError`, lo que evita que el programa se bloquee si el usuario escribe letras o símbolos donde se espera un número.

Finalmente, la función `main()` integra todo. Carga el inventario al inicio, muestra el menú en bucle y dirige la entrada del usuario a la función correspondiente. Tras cualquier operación que modifique el inventario, se llama inmediatamente a `save_csv()` para conservar los cambios.

### `test_project.py`

Este archivo contiene las pruebas unitarias del proyecto, puede implementarse con `pytest`. Prueba tres funciones principales: `add_products()`, `delete()` y `update()`.

La función `test_add_products()` crea una lista de inventario vacía, llama a `add_products()` con datos de muestra y luego utiliza declaraciones `assert` para verificar que el producto se agregó correctamente y que la ID generada automáticamente es 1.

La función `test_delete()` añade un producto a una lista y luego llama a `delete()`, reasignando el resultado a `inventory`. A continuación, confirma que el inventario está vacío, lo que confirma que el producto se eliminó.

La función `test_update()` modifica directamente el campo de un producto en el diccionario de inventario y confirma que se aplicó el cambio. Dado que `update()` depende internamente de `input()`, probarla directamente provocaría que el programa se bloqueara esperando la entrada del usuario, por lo que se prueba la lógica subyacente de forma directa.

### `requirements.txt`

Este archivo enumera las dependencias externas necesarias para ejecutar el proyecto. La única dependencia es `pytest`, que se utiliza exclusivamente para ejecutar el conjunto de pruebas. El resto del proyecto se basa completamente en la biblioteca estándar de Python (csv).

## Decisiones de diseño

Una de las principales decisiones de diseño fue usar una **lista de diccionarios** en lugar de una clase personalizada (*class*) para representar los productos.Decidí esto porque los productos solo guardan datos, no tienen comportamiento propio como lo podría tener un objeto. Las distintas operaciones con los productos, como añadir, editar y eliminar, se gestionan mediante funciones independientes que reciben la lista de inventario como parámetro. Esto también facilita la prueba de las funciones con `pytest`.

Otra decisión fue **guardar en CSV después de cada operación** en lugar de solo al salir el usuario. Esto garantiza que no se pierdan datos si el programa se cierra inesperadamente, por ejemplo, al cerrar la terminal directamente.

La elección de usar **CSV en lugar de JSON o una base de datos** fue intencional. CSV es uno de los temas centrales que se tratan en CS50P, es legible y suficiente para el alcance de este proyecto. También permite abrir e inspeccionar fácilmente el archivo de inventario en cualquier aplicación de hoja de cálculo.

## Autor
Enrique Damian Suica — CS50P Final Project (2026)
Harvard University — Introduction to Programming with Python