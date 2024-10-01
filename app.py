import py5

# Variables globales
arr = []
n = 50  # Número de elementos a ordenar
delay = 50  # Retraso en milisegundos para la animación
sorting = False  # Controla si la animación está en progreso
sort_type = "bubble"  # Tipo de algoritmo de ordenamiento ("bubble" o "quick")
completed = False  # Bandera para saber si el ordenamiento ha terminado


def setup():
    global arr
    py5.size(800, 600)
    generate_new_array()
    py5.no_loop()  # Inicia sin animación hasta que se presione una tecla


def draw():
    global arr
    py5.background(255)
    draw_array(arr, [])


def generate_new_array():
    """Genera una nueva lista desordenada de valores aleatorios."""
    global arr, completed
    arr = [py5.random(50, 550) for _ in range(n)]
    completed = False


def draw_array(arr, highlights):
    """Dibuja la lista como una serie de rectángulos (barras)."""
    bar_width = py5.width / len(arr)
    for i in range(len(arr)):
        if i in highlights:
            py5.fill(255, 0, 0)  # Colorear elementos resaltados (comparación/intercambio)
        else:
            py5.fill(100, 100, 255)  # Color normal de los elementos
        py5.rect(i * bar_width, py5.height - arr[i], bar_width, arr[i])


def bubble_sort_step(arr):
    """Genera los pasos de Bubble Sort con comparaciones e intercambios."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr, [j, j + 1]  # Retorna el estado actual del array y los elementos comparados


def quick_sort_step(arr, low, high):
    """Genera los pasos de Quick Sort con comparaciones e intercambios."""
    if low < high:
        pi = partition(arr, low, high)
        yield from quick_sort_step(arr, low, pi - 1)
        yield from quick_sort_step(arr, pi + 1, high)


def partition(arr, low, high):
    """Función auxiliar para Quick Sort."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        yield arr, [i, j, high]  # Retorna el estado del array y los elementos comparados
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def key_pressed():
    """Controla el inicio, reinicio o cambio de algoritmo."""
    global sorting, sort_type, completed
    if py5.key == ' ' and not sorting:  # Iniciar/continuar ordenamiento
        sorting = True
        py5.loop()  # Activa el bucle de Py5 para animar
    elif py5.key == 'r':  # Reiniciar con una nueva lista
        sorting = False
        generate_new_array()
        py5.redraw()
        py5.no_loop()
    elif py5.key == 'b':  # Cambiar a Bubble Sort
        sort_type = "bubble"
        sorting = False
        generate_new_array()
        py5.redraw()
        py5.no_loop()
    elif py5.key == 'q':  # Cambiar a Quick Sort
        sort_type = "quick"
        sorting = False
        generate_new_array()
        py5.redraw()
        py5.no_loop()


def sort_animation():
    """Controla el ciclo de animación de los algoritmos de ordenamiento."""
    global sorting, completed
    if sorting and not completed:
        if sort_type == "bubble":
            sort_steps = bubble_sort_step(arr)
        elif sort_type == "quick":
            sort_steps = quick_sort_step(arr, 0, len(arr) - 1)

        try:
            arr_state, highlights = next(sort_steps)
            draw_array(arr_state, highlights)  # Dibuja los elementos comparados
            py5.delay(delay)
        except StopIteration:
            completed = True  # El ordenamiento está completo
            sorting = False
            py5.no_loop()


# Función de Py5 que se ejecuta continuamente mientras el bucle está activo
def draw():
    sort_animation()


py5.run_sketch()
