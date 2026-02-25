from typing import List

def maxProfit(prices: List[int]) -> int:
    """
    Fuerza bruta: probar todas las combinaciones (compra en i, venta en j>i).

    Tiempo: O(n^2)  -- dos bucles anidados que recorren pares (i, j).
    Espacio: O(1)   -- uso constante de memoria adicional (solo variables auxiliares).

    Args:
        prices: lista de enteros con precios por día.

    Returns:
        Máxima ganancia posible (int). Si no hay ganancia, 0.
    """
    n = len(prices)
    mejor = 0
    for i in range(n):
        for j in range(i + 1, n):
            ganancia = prices[j] - prices[i]
            if ganancia > mejor:
                mejor = ganancia
    return mejor


if __name__ == "__main__":
    
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Ejemplo 1 falló"
    assert maxProfit([7, 6, 4, 3, 1]) == 0, "Ejemplo 2 falló"
    assert maxProfit([]) == 0, "Vacío -> 0"
    assert maxProfit([5]) == 0, "Un solo día -> 0"
    assert maxProfit([2, 2, 2]) == 0, "Constantes -> 0"
    assert maxProfit([1, 2]) == 1, "Subida simple"

    print("All brute force tests passed.")