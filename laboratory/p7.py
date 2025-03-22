import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([30, 60, 90, 120, 150, 180, 210, 240, 270, 300])   # uso del celular
y_arr = nparr([10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5])   # duración de la batería

# Variables
var_ind = "Tiempo de uso del Celular (mins)"
var_dep = "Duración de la Batería (hrs)"
titulo_diagrama = "Diagrama de dispersión de la Duración de la Batería (hrs) vs el Tiempo de uso del Celular (mins)"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
