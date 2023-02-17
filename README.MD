# Libreria total complejos.
Se realizó con éxito los siguientes programas:
1. Adición de vectores complejos.
2. Inverso (aditivo) de un vector complejos.
3. Multiplicación de un escalar por un vector complejo.
4. Adición de matrices complejas.
5. Inversa (aditiva) de una matriz compleja.
6. Multiplicación de un escalar por una matriz compleja.
7. Transpuesta de una matriz/vector
8. Conjugada de una matriz/vector
9. Adjunta (daga) de una matriz/vector
10. Producto de dos matrices (de tamaños compatibles)
11. Función para calcular la "acción" de una matriz sobre un vector.
12. Distancia entre dos vectores
13. Valores  y vectores propios de una matriz
14. Revisar si una matriz es unitaria
15. Revisar si una matriz es Hermitiana
16. Producto tensor de dos matrices/vectores
    
*Obteniendo un error con los programas:*
1. Producto interno.
2. Norma de un vector.
   
   Se sigue la definición de producto interno pero se llegan a valores imaginarios al establecer la norma de un vector


## Pruebas.py
Lamentablemente no logramos establecer una solución para la ejecución de este programa vital para la evaluacipon de la libreria. Nos encontramos con el error:

```python
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```

Sin embargo, implementamos *all* para la mayoria de funciones:
```python
result1 = cp.sumavec(a, b)
if result1 == all(result1):
    passed +=1
else:
    failed += 1
```
 *consulte las demás funciones en archivo pruebas.py*
Y no obtuvimos solución al error.
