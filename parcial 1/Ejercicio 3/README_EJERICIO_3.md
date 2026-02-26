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

---

## Solución 2: Optimizada (un recorrido)

### Idea

Recorrer el arreglo una sola vez:

* Mantener el **precio mínimo** visto hasta ahora.
* Calcular la ganancia si vendemos hoy.
* Actualizar la mejor ganancia.

### Implementación

```python
from typing import List

def max_profit_optimized(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for p in prices[1:]:
        ganancia = p - min_price

        if ganancia > max_profit:
            max_profit = ganancia

        if p < min_price:
            min_price = p

    return max_profit
```

### Complejidad

* **Tiempo:** O(n) → un solo recorrido.
* **Espacio:** O(1) → memoria constante.

### Cuándo usarla

✔ Solución óptima para entradas grandes.
✔ Estándar en entrevistas y programación competitiva.

---

## Comparación

| Criterio   | Fuerza Bruta | Optimizada |
| ---------- | ------------ | ---------- |
| Tiempo     | O(n²)        | O(n)       |
| Espacio    | O(1)         | O(1)       |
| Dificultad | Fácil        | Media      |
| Uso real   | ❌            | ✅          |

---

## Análisis y patrones utilizados

Este ejercicio utiliza el patrón:

### 🔹 **Min/Max en un recorrido**

Mantener el valor mínimo observado para calcular el mejor resultado posible en tiempo lineal.

Este patrón aparece frecuentemente en:

* problemas financieros
* máximas ganancias
* diferencias máximas
* ventanas de optimización

---

## Resumen

* El problema busca maximizar la ganancia con una sola compra y venta.
* La solución por fuerza bruta es O(n²).
* La solución óptima usa un recorrido lineal O(n).
* Mantener el mínimo precio visto permite calcular la mejor ganancia eficientemente.
* Es un problema clásico de entrevistas técnicas.

---
