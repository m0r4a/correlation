from rich.console import Console
from rich.table import Table
from rich import box

def table(title, value, conclusion) -> None:
    """
    Crea y muestra una tabla de 2 filas y 1 columna

    Parámetros:
      - title: String que representa el título o primera fila.
      - value: String que representa el valor de r o segunda fila.
      - conclusion: Conclusión del problema.

    """
    if type(title) != str or type(value) != str or type(conclusion) != str:
        title, value, conclusion = map(str, (title, value, conclusion))

    console = Console()

    table = Table(show_header=False, box=box.ROUNDED, style="white")

    table.add_column()

    table.add_row(title)
    table.add_section()
    table.add_row(value)
    table.add_section()
    table.add_row(conclusion)

    console.print(table)
