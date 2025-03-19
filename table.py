from rich.console import Console
from rich.table import Table
from rich import box

def table(title, content) -> None:
    """
    Crea y muestra una tabla de 2 filas y 1 columna

    Parámetros:
      - title: String que representa el título o primera fila.
      - content: String que representa el contenido o segunda fila.
    """
    if type(title) != str or type(content) != str:
        title, content = map(str, (title, content))

    console = Console()

    table = Table(show_header=False, box=box.ROUNDED, style="white")

    table.add_column()

    table.add_row(title)
    table.add_section()
    table.add_row(content)

    console.print(table)
