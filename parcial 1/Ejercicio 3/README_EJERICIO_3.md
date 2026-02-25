# Best Time to Buy and Sell Stock (LeetCode)

Problema tomado de LeetCode.

---

## Enunciado

Dado un arreglo `prices` donde `prices[i]` es el precio de una acción en el día `i`, devolver la **máxima ganancia posible** eligiendo un día para comprar y un día **posterior** para vender.

Si no es posible obtener ganancia, devolver `0`.

---

## Ejemplo(s)

**Ejemplo 1**

Entrada:

```
prices = [7, 1, 5, 3, 6, 4]
```

Salida:

```
5
```

Explicación: comprar en 1 y vender en 6.

**Ejemplo 2**

Entrada:

```
prices = [7, 6, 4, 3, 1]
```

Salida:

```
0
```

Explicación: el precio siempre baja.

---

## Solución 1: Fuerza bruta

### Idea

Probar todas las combinaciones posibles de compra y venta `(i, j)` con `i < j` y calcular la ganancia.

### Implementación

```python
from typing import List

def max_profit_brute_force(prices: List[int]) -> int:
    mejor = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            ganancia = prices[j] - prices[i]
            if ganancia > mejor:
                mejor = ganancia

    return mejor
```

### Complejidad

* **Tiempo:** O(n²) → se evalúan todos los pares posibles.
* **Espacio:** O(1) → solo variables auxiliares.

### Cuándo usarla

✔ Para entender el problema.
✔ Para verificar la lógica con entradas pequeñas.
❌ No recomendable para entradas grandes.