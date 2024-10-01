# PROYECTO: Algoritmos de Ordenamiento y Visualización en Py5

## Descripción:
Este proyecto implementa dos algoritmos de ordenamiento, Bubble Sort y Quick Sort, y
visualiza su proceso mediante animaciones interactivas utilizando la biblioteca Py5.
El objetivo principal es mostrar cómo funcionan estos algoritmos de forma visual,
resaltando las comparaciones e intercambios de elementos durante el proceso de
ordenamiento.

## Requisitos:
- Python 3.x
- Biblioteca Py5 (instalar con: pip install py5)

## Archivos:
- main.py: Código fuente que contiene la implementación de los algoritmos y la visualización.
- README.txt: Este archivo.

## Instrucciones de Uso:
1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca Py5 ejecutando el siguiente comando en tu terminal:
   pip install py5
3. Ejecuta el script principal `main.py` para iniciar la visualización.

## Controles Interactivos:
- Espacio (' '): Inicia o reanuda la animación del algoritmo de ordenamiento.
- Tecla 'r': Reinicia la visualización con una nueva lista aleatoria de valores.
- Tecla 'b': Cambia al algoritmo Bubble Sort y reinicia la animación.
- Tecla 'q': Cambia al algoritmo Quick Sort y reinicia la animación.

## Algoritmos de Ordenamiento:
1. Bubble Sort:
   - Compara cada par de elementos adyacentes en la lista y los intercambia si están
     en el orden incorrecto. El proceso se repite hasta que la lista está completamente
     ordenada.
2. Quick Sort:
   - Selecciona un pivote y reorganiza los elementos para que todos los menores que el
     pivote queden a su izquierda y los mayores a su derecha. Luego, aplica el mismo
     proceso recursivamente en las sublistas.

## Visualización:
- Los elementos de la lista desordenada se representan como barras de diferentes tamaños.
- Durante la ejecución de los algoritmos, las barras que se están comparando e
  intercambiando se resaltan en color rojo.
- El proceso continúa hasta que todos los elementos están ordenados.

## Personalización:
- Puedes ajustar el número de elementos a ordenar cambiando la variable `n` en el código.
- También puedes modificar la velocidad de la animación ajustando el valor de `delay`.
