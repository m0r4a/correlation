import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])   # cantidad de empleados
y_arr = nparr([100, 200, 290, 370, 450, 530, 600, 670, 740, 800])   # producción mensual

# Variables
var_ind = "Cantidad de Empleados"
var_dep = "Producción Mensual de una Fábrica"
titulo_diagrama = "Diagrama de dispersión de la Producción Mensual de una Fábrica vs la Cantidad de Empleados"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
