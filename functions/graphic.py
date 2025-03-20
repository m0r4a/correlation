import matplotlib.pyplot as plt
import numpy as np
import warnings

def show_ascii_plot(x_arr, y_arr, nombre_var_ind, nombre_var_dep, titulo_diagrama, color):
    """
    Muestra un gráfico de dispersión en la terminal usando plotext.

    Parámetros:
      - x_arr, y_arr: Datos a graficar.
      - title: Título del gráfico.
      - color: color del marker
    """
    try:
        import plotext as plt_ascii
        x, y = x_arr.tolist(), y_arr.tolist()
        plt_ascii.scatter(x, y, color=color, marker='hd')
        plt_ascii.title(titulo_diagrama)
        plt_ascii.theme("clear")
        plt_ascii.plot_size(180, 40)
        plt_ascii.xlabel(nombre_var_ind)
        plt_ascii.ylabel(nombre_var_dep)
        plt_ascii.show()
    except ImportError:
        print("Para la salida ASCII, instala plotext: pip install plotext")


def graphic(x_arr, y_arr, nombre_var_ind="Eje X", nombre_var_dep="Eje Y", titulo_diagrama="Diagrama de dispersión", color="mediumslateblue", save_path="./diagrama_dispersion.png", ascii_output=False):
    """
    Crea un diagrama de dispersión comparando dos arreglos numéricos.

    Parámetros:
      - x_arr: arreglo del eje X a graficar (var independiente).
      - y_arr: arreglo del eje Y a graficar (var dependiente).
      - save_path: Ruta para guardar la imagen (ej: 'grafico.png').
      - ascii_output: Si es True, muestra la salida en ASCII.
    """
    # Esta List Comprehension itera sobre ambos arreglos y verifica si alguno
    # no es un numpy array; en ese caso, lo convierte.
    x_arr, y_arr = (np.array(a) if not isinstance(a, np.ndarray) else a for a in (x_arr, y_arr))
    nombre_var_ind, nombre_var_dep = (str(a) if not type(a) == str else a for a in (nombre_var_ind, nombre_var_dep))

    if ascii_output:
        show_ascii_plot(x_arr, y_arr, nombre_var_ind, nombre_var_dep, titulo_diagrama, color)
        return

    # Se fuerza el uso del estilo 'dark_background' para darkmode,
    # ignorando cualquier otro estilo que se pase en kwargs.
    plt.style.use('ggplot')

    plt.figure(figsize=(10, 5))
    plt.scatter(x_arr, y_arr, color=color, label="Datos")

    plt.title(titulo_diagrama)
    plt.xlabel(nombre_var_ind)
    plt.ylabel(nombre_var_dep)
    plt.grid(True)
    plt.legend()

    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=UserWarning)
                plt.show()
        except UserWarning as e:
            print(f"Error al mostrar el gráfico con Matplotlib: {e}\nIntenando salida ASCII...")
            show_ascii_plot(x_arr, y_arr, nombre_var_ind, nombre_var_dep, titulo_diagrama, color)
