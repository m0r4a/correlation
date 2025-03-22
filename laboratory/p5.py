import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])   # distancia recorrida
y_arr = nparr([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])   # combustible consumido

# Variables
var_ind = "Distancia Recorrida (km)"
var_dep = "Combustible Consumido (litros)"
titulo_diagrama = "Diagrama de dispersión del Combustible Consumido (litros) vs la Distancia recorrida (km)"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
