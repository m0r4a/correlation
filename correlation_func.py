import numpy as np
from scipy import stats

def correlation(arr1, arr2, method='pearson'):
    """
    Calcula la correlación entre dos arreglos usando el método especificado.

    Parámetros:
      - arr1, arr2: Arreglos (o listas) de datos numéricos.
      - method: Método de correlación a utilizar. Acepta:
          • 'r', 'pearson', 'pearsonr'  → Correlación de Pearson.
          • 's', 'spearman', 'spear'    → Correlación de Spearman.
          • 'k', 'kendall'              → Correlación de Kendall tau.

    Retorna:
      - Una tupla (coeficiente, valor_p) según la función estadística correspondiente.
    """

    arr1, arr2 = (np.array(a) if not isinstance(a, np.ndarray) else a for a in (arr1, arr2))

    methods = {
        'r': stats.pearsonr,
        'pearson': stats.pearsonr,
        'pearsonr': stats.pearsonr,
        's': stats.spearmanr,
        'spearman': stats.spearmanr,
        'spear': stats.spearmanr,
        'k': stats.kendalltau,
        'kendall': stats.kendalltau
    }

    # convert the method to lower
    method_key = method.lower()

    # check if the method exists
    if method_key not in methods:
        raise ValueError(f"El método: {method} no existe.\nElige entre: {list(methods.keys())}")

    # execute the method
    func = methods[method_key]
    result = func(arr1, arr2)

    return result
