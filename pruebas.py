import complejos as cp
import math
#Prueba liberia complejos.

passed = 0
failed = 0

#Diferentes matrices.
#suma vectores
a = [1,2+3j, 4j]
b = [5j+1,+1j+3j,3j]

result1 = cp.sumavec(a, b)
if result1 == all(result1):
    passed +=1
else:
    failed += 1

#Inverso aditivo
result2 = cp.inverso(a)
if result2 == all(result2):
    passed += 1
else:
    failed +=1

#MultiplicaciónEscalar
result3 = cp.escalarComplejo(2, a)
if result3 == [(2+6j), 8j, 10j]:
    passed += 1
else:
    failed +=1

#Adición de matrices complejas.
result4 = cp.sumaMatricesComplejos(a,b)
if result4 == all(result4):
    passed +=1
else:
    failed +=1

#Inversa (aditiva) de una matriz compleja.
result5 = cp.inversaDeUnaMatriz([[1+3j,4j,5j],[5j+1,+1j+3j,3j],[1,2,3]])
if result5 == all(result5):
    passed +=1
else:
    failed +=1

#Multiplicación de un escalar por una matriz compleja.
result6 = cp.escalarPorComplejo(3, [[1+3j,4j,5j],[5j+1,+1j+3j,3j],[1,2,3]])
if result6 == [[(3+9j), 12j, 15j], [(3+15j), 12j, 9j], [3, 6, 9]]:
    passed += 1
else:
    failed +=1

#Transpuesta
result7 = cp.traspuesta([[1+3j,4j,5j],[5j+1,+1j+3j,3j],[1,2,3]])
if result7 == [[1.+3.j, 1.+5.j, 1.+0.j],[0.+4.j, 0.+4.j, 2.+0.j],[0.+5.j, 0.+3.j, 3.+0.j]]:
    passed +=1
else:
    failed +=1

#Conjugada de una matriz/vector
result8 = cp.conjugada([[1+3j,4j,5j],[5j+1,+1j+3j,3j],[1,2,3]])
if result8 == [[1.+3.j, 1.+5.j, 1.+0.j], [0.+4.j, 0.+4.j, 2.+0.j],[0.+5.j, 0.+3.j, 3.+0.j]]:
    passed +=1
else:
     failed += 1

#Adjunta (daga) de una matriz/vector
result9 = cp.adjunta([[1+3j,4j,5j],[5j+1,+1j+3j,3j],[1,2,3]])
if result9 == [[1.-3.j, 1.-5.j, 1.-0.j],[0.-4.j, 0.-4.j, 2.-0.j], [0.-5.j, 0.-3.j, 3.-0.j]]:
    passed +=1
else:
    failed +=1

#Producto de dos matrices
result10 = cp.producto_matrices([[1,2+3j, 4j]], [[5j+1],[1j+3j],[3j]])
if result10 == [[-23.+13.j]]:
    passed +=1
else:
    failed +=1

#Función para calcular la "acción" de una matriz sobre un vector.
result11 = cp.accionmatrix()
if result11 == [[  1. +5.j, -13.+13.j, -20. +4.j],[  0. +4.j, -12. +8.j, -16. +0.j],[  0. +3.j, -9. +6.j, -12. +0.j]]:
    passed += 1
else:
    failed +=1

#Producto interno de dos vectores
result12 = cp.productoInternoVectores([1,2+3j, 4j], [5j+1,+1j+3j,3j])
if result12 == (25-13j):
    passed +=1
else:
    failed +=1

#Norma de un vector
result13= cp.normaVector([1,2+3j, 4j],)
if result13 == (5.477225575051661+0j):
    passed += 1
else:
    failed += 1

#Distancia entre dos vectores
result14 = cp.distanceVectors([1,2+3j, 4j],[5j+1,+1j+3j,3j])
if result14 == math.sqrt(31.0):
    passed += 1
else:
    failed +=1

#Valores  y vectores propios de una matriz
result15 = cp.valuesAndVectosProp([[4,5,6],[7,8,2],[-1,4,5]])

#Revisar si una matriz es unitaria
result16= cp.matrixunitaria([[1,0,0],[0,1,0],[0,0,1]])
if result16 == "Es unitaria":
    passed +=1
else:
    failed +=1

#Revisar si una matriz es Hermitiana
result17= cp.hermitiana([[-1,-1j],[1j,1]])
if result17 == "Es hermitiana":
    passed +=1
else:
    failed +=1


#Producto tensor de dos matrices/vectores
result18 = cp.producTen([[1,2+3j, 4j]], [[5j+1],[1j+3j],[3j]])
if result18 == [[(1+5j), (-13+13j), (-20+4j)], [4j, (-12+8j), (-16+0j)], [3j, (-9+6j), (-12+0j)]]:
    passed += 1
else:
    failed +=1