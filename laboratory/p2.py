import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([15, 18, 20, 22, 25, 28, 30, 32, 35, 38])   # temperatura ambiental
y_arr = nparr([50, 70, 90, 120, 150, 180, 210, 250, 280, 320])   # cantidad de helados

# Variables
var_ind = "Temperatura ambiental (°C)"
var_dep = "Cantidad de helados vendidos"
titulo_diagrama = f"Diagrama de dispersión\n{var_dep} vs {var_ind}"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
