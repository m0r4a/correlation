from numpy import array as nparr
from functions.table import table
from functions.graphic import graphic
from functions.coeficiente_correlacion import calcular_coeficiente_correlacion

# Arreglos de prueba
x_arr = nparr([10, 12, 8, 17, 10, 15, 10, 14, 19, 10, 11, 13, 16, 10, 12])
y_arr = nparr([15, 17, 13, 23, 16, 21, 14, 20, 24, 17, 16, 18, 23, 15, 16])

# Variables de prueba
var_dep = "cantidad de pasajeros"
var_ind = "cantidad gastada en publicidad"

r, conclusion = calcular_coeficiente_correlacion(x_arr, y_arr, var_dep, var_ind)

table("Pearson r value", r, conclusion)
graphic(x_arr, y_arr, save_path="./diagrama_dispersion.png")

# -----------------------------------------------------------
# Medir correlación lineal (datos que cumplen normalidad)
#
# La correlación de Pearson se usa cuando:
# - Los datos son continuos y aproximadamente normales.
# - Buscas evaluar una relación lineal entre las variables.
# La función stats.pearsonr retorna el coeficiente de correlación y el valor p.
#
# Si no se observa una relación lineal entonces se dice que dado
# que no hay una correlación lineal entre la var. dependiente y la
# var. independiente el coeficiente de Pearson no proporciona información
# suficiente para determinar la correlación en casos de relación no lineal.
# -----------------------------------------------------------
