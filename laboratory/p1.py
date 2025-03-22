import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

# Arreglos de prueba
x_arr = nparr([20, 22, 25, 27, 30, 32, 35, 37, 40,  42, 45, 47, 50, 52, 55, 57])
y_arr = nparr([180, 185, 195, 200, 210, 220, 230, 240, 255, 270, 290, 310, 330, 350, 370, 390])

# Variables de prueba
var_ind = "Edad de la persona (años)"
var_dep = "Tiempo de Reacción (ms)"
titulo_diagrama = "Diagrama de dispersión del Tiempo de Reacción (ms) vs la Edad de la persona (años)"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
