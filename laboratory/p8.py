import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])   # publicaciones
y_arr = nparr([100, 250, 400, 600, 850, 1100, 1400, 1750, 2150, 2600])   # seguidores

# Variables
var_ind = "Número de Publicaciones"
var_dep = "Cantidad de Seguidores Obtenidos"
titulo_diagrama = f"Diagrama de dispersión\n{var_dep} vs {var_ind}"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
