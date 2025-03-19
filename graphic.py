import matplotlib.pyplot as plt
import numpy as np
import warnings

def show_ascii_plot(arr1, arr2, color):
    """
    Muestra un gráfico de dispersión en la terminal usando plotext.

    Parámetros:
      - arr1, arr2: Datos a graficar.
      - title: Título del gráfico.
      - **kwargs: Argumentos adicionales (xlabel, ylabel, color).
    """
    try:
        import plotext as plt_ascii
        x, y = arr1.tolist(), arr2.tolist()
        plt_ascii.scatter(x, y, color=color, marker='hd')
        plt_ascii.title("Gráfico de dispersión")
        plt_ascii.theme("clear")
        plt_ascii.plot_size(180, 40)
        plt_ascii.xlabel('Eje X')
        plt_ascii.ylabel('Eje Y')
        plt_ascii.show()
    except ImportError:
        print("Para la salida ASCII, instala plotext: pip install plotext")


def graphic(arr1, arr2, color="mediumslateblue", save_path=None, ascii_output=False):
    """
    Crea un diagrama de dispersión comparando dos arreglos numéricos.

    Parámetros:
      - arr1: arreglo del eje X a graficar.
      - arr2: arreglo del eje Y a graficar.
      - title: Título del gráfico.
      - save_path: Ruta para guardar la imagen (ej: 'grafico.png').
      - ascii_output: Si es True, muestra la salida en ASCII.
    """
    # Esta List Comprehension itera sobre ambos arreglos y verifica si alguno
    # no es un numpy array; en ese caso, lo convierte.
    arr1, arr2 = (np.array(a) if not isinstance(a, np.ndarray) else a for a in (arr1, arr2))

    if ascii_output:
        show_ascii_plot(arr1, arr2, color)
        return

    # Se fuerza el uso del estilo 'dark_background' para darkmode,
    # ignorando cualquier otro estilo que se pase en kwargs.
    plt.style.use('dark_background')

    plt.figure(figsize=(10, 5))
    plt.scatter(arr1, arr2, color=color, label="Datos")

    plt.title("Gráfico de dispersión")
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
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
            show_ascii_plot(arr1, arr2, color)
