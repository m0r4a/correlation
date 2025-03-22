import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])   # inversión en publicidad
y_arr = nparr([50, 100, 160, 220, 290, 360, 450, 540, 630, 720, 810, 900, 1000, 1100, 1200, 1300])   # ventas

# Variables
var_ind = "Dinero Invertido en Publicidad"
var_dep = "Ventas Mensuales"
titulo_diagrama = f"Diagrama de dispersión\n{var_dep} vs {var_ind}"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
