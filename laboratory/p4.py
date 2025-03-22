import sys
import os
from numpy import array as nparr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "functions")))

from table import table
from graphic import graphic
from coeficiente_correlacion import calcular_coeficiente_correlacion

x_arr = nparr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])            # número de horas
y_arr = nparr([50, 55, 65, 70, 80, 85, 90, 92, 95, 97])   # calificaciones

# Variables
var_ind = "Número de Horas dedicadas a estudiar"
var_dep = "Calificación en un Examen"
titulo_diagrama = "Diagrama de dispersión de la Calificación en un Examen vs el Número de horas dedicadas a estudiar"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_ind, var_dep)

table("Pearson r value", r, conclusion)

problem_number, _ = sys.argv[0].split(".")

graphic(x_arr, y_arr, var_ind, var_dep, titulo_diagrama, save_path=f"diagramas/{problem_number}_diagrama_dispersion")
