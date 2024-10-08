Comentarios para mirar el código del "Sistema de formulación".

* El código no está comentado, recibo consejos de cómo se debe hacer.
* La versión de python instalada es: Python 3.12.4.
* No se instalaron librerias, las usadas están incluidas en python.

Instrucciones para ver el programa funcionando:
1. ejecutar el archivo "models.py" creará la base de datos con las tablas vacias.
2. ejecutar el archivo "seeder.py" para agregar algunos datos a la base de datos.
3. ejecutar el archivo "main.py" para correr el programa e interactuar con la insterfaz.

Las funcionalidades del programa no son completamente intuitivas, más adelante se harán 
cambios en:

* Las opciones "Crear una fórmula" y "Editar una fórmula" no cumplen las tareas deseadas 
  completamente.

* La opción "Crear una fórmula" solo guarda el nombre de un producto, se presiona ENTER para
  añadirlo.

* La opción "Editar una fórmula" no edita fórmulas ya creadas, solo añade los datos necesario
  para completar la fórmula de un producto.
  Al ingresar un componente y un porcentaje se presiona ENTER en la casilla del porcentaje
  para guardar estos dos datos.
  Al ingresar una instrucción se presiona ENTER en esa casilla para guardarla.

* Crear un botton de "HOME".

* Crear un botton para retroceder a la pantalla anterior y posiblemente uno para la
  siguiente pantalla (en el caso que ya se haya retrocedido).