from numpy import array as nparr
from table import table
from correlation_func import correlation
from graphic import graphic

# Define tus datos aquí (reemplaza los [...] con tus datos)
x_arr = nparr([...])
y_arr = nparr([...])

# Arreglos de prueba
# x_arr = nparr([10, 12, 8, 17, 10, 15, 10, 14, 19, 10, 11, 13, 16, 10, 12])
# y_arr = nparr([15, 17, 13, 23, 16, 21, 14, 20, 24, 17, 16, 18, 23, 15, 16])


value, p_val = correlation(x_arr, y_arr)
table("Pearson r value", value)
graphic(x_arr, y_arr)

# -----------------------------------------------------------
# 1. Medir correlación lineal (datos que cumplen normalidad)
#
# Utiliza la correlación de Pearson cuando:
# - Los datos son continuos y aproximadamente normales.
# - Buscas evaluar una relación lineal entre las variables.
#
# La función stats.pearsonr retorna el coeficiente de correlación y el valor p.
# -----------------------------------------------------------

# -----------------------------------------------------------
# 2. Medir correlación basada en rangos (datos no necesariamente normales)
#
# Utiliza la correlación de Spearman cuando:
# - Los datos no son normales o la relación puede no ser lineal.
# - Se evalúa la relación en función de los rangos de los datos.
#
# La función stats.spearmanr retorna el coeficiente y el valor p.
# -----------------------------------------------------------

# -----------------------------------------------------------
# 3. Medir correlación ordinal (ideal para datos ordinales)
#
# Utiliza la correlación de Kendall tau cuando:
# - Se trabaja con datos ordinales.
# - Se quiere evaluar la relación basada en la concordancia de pares.
#
# La función stats.kendalltau retorna el coeficiente y el valor p.
# -----------------------------------------------------------
