#Hill Climbing
#Yithzak Alarcon - T00045029
import string, math, random
import numpy as np
from numpy import e
def distancesFromCoords():
    f = open('kroA100.tsp')
    data = [line.replace("\n","").split(" ")[1:] for line in f.readlines()[6:106]]
    coords =  list(map(lambda x: [float(x[0]),float(x[1])], data))
    distances = []
    for i in range(len(coords)):
        row = []
        for j in range(len(coords)):
            row.append(math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2))
        distances.append(row)
    return distances

#Definimos una función general para 
#generar la perturbación en un vector
def pertVec(H):
    a = random.randint(1, len(H)-2) 
    b = random.randint(1, len(H)-2)
    while(b == a):
        b = random.randint(1, len(H)-2)
    for i in range(1,len(H)-1):
        if(a == H[i]):
            pos_a = i
            mag_a = H[i]        
        elif(b == H[i]):
            pos_b = i
            mag_b = H[i]
    H[pos_b] = mag_a
    H[pos_a] = mag_b
    return H

#Definimos una función general para realizar
#la suma de una solución cualquiera
def suma(M, V):
    Sum = 0
    Ide = np.zeros(len(V),float)
    for i in range(0,len(V)-1):
        Ide[i] = M[V[i]][V[i+1]]
        Sum += Ide[i]
    return Sum

#Guardamos la matriz de adyacencia en una variable
M = distancesFromCoords()
#print(M);
n = len(M)
#Definimos el vector con la referencia de todas las ciudades
V = np.arange(0,n+1,1,dtype=int)
V[n] = 0
#Definimos un arreglo auxiliar para almacenar los datos del Numpy Array V
Vaux = []
for j in range(0,len(V)):
    Vaux += [V[j]]

#Definimos las condiciones iniciales para el recocido simulado    
Iteracion = 1300
alpha = 0.9999
print(Vaux)
#Independizamos las listas de forma de poder perturbar una solución
#Y que no afecte a la otra
Vec1 = Vaux[:]
#Bucle While que comienza el proceso de iterado y perturbación
while(Iteracion > 0.01):
    Vec2 = Vec1[:]
    pertVec(Vec2)
    if(suma(M,Vec2) < suma(M,Vec1)):
        Vec1 = Vec2[:]
    Iteracion = Iteracion * alpha
    print("\nSuma: ",suma(M,Vec1))
print("\nSolucion optima: \n\n", Vec1)







