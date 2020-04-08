import string, math, random

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
def z_x(a):
    i=0
    for i in range(100):
        if i==0:
            x=M[a[i]][a[i+1]]
        else:
            x+=M[a[i]][a[i+1]]
    return x
#Autores: Cesar Sierra Pardo y Yithzak Alarcon
M=distancesFromCoords() #Matriz de adyacencia
N=1000000
Tao = [[0]*100 for i in range(N)] #Matriz de feromonas
Nu = [[0]*100 for i in range(N)] #Matriz de heuristica local

for i in range(N):
    cities = random.sample(range(100), 100) #Crea un vector aleatorio
    cities.append(cities[0])
    #Route[i][:]=cities
    Z=z_x(cities)
    for i in range(100):
        Tao[cities[i]][cities[i+1]]+=1/Z
        Tao[cities[i+1]][cities[i]]+=1/Z

for i in range(100):
    for j in range(100):
        if(i!=j):
            Nu[i][j]=1/M[i][j]
            
Ciudad_inicio=0
alpha=3
beta=3
ro=0.2
HG=100000
Z_min=200000
C_act = Ciudad_inicio
for i in range(HG):
    route= [Ciudad_inicio]*1
    c_restantes = random.sample(range(100), 100)#Crea un vector de 1 a 100
    c_restantes.remove(Ciudad_inicio)
    c_restantes.sort(reverse=True)
    c_restantes.reverse()
    for m in range(98):
        #c_restantes.remove(10)
        suma_act = 0
        ver_sum = 0

        #Calcular la sumatoria para calcular la probabilidad de cada ruta
        for i in range(len(c_restantes)):
            suma_act += ((Tao[C_act][c_restantes[i]])**alpha)*((Nu[C_act][c_restantes[i]])**beta)
            
        prob = [0*1 for i in range(len(c_restantes))]#Defino el vector p

        #Se definió el vector de probabilidades con las matrices de heurística y feromonas
        if(suma_act!=0):
            for j in range(len(c_restantes)):
                prob[j] = ((Tao[C_act][c_restantes[j]])**alpha)*((Nu[C_act][c_restantes[j]])**beta)/suma_act
        else: 
            break
        count = -1

        #Generamos número aleatorio
        num = random.random()
        sum_prob = 0
        bandera=True

        #Ciclo para definir la posición de la siguiente ciudad dependiendo de su probabilidad
        while(bandera):

            if(num<sum_prob):

                bandera=False

            else:
                count += 1
                sum_prob+= prob[count]
                

        #Añadir nueva ciudad en el vector route
        route.append(c_restantes[count])
        C_act = c_restantes[count]#Actualizar la ciudad actual
        c_restantes.remove(c_restantes[count])#Remover la ciudad actual de las posibles

        if(len(c_restantes)==1):#Si solo resta una posible ciudad, añadirla a la ruta
            route.append(c_restantes[0])
            route.append(Ciudad_inicio)#Añadir la ciudad inicial
            
    #Actualizar la matriz de feromonas
    if(suma_act!=0):
        Z=z_x(route)
        if(Z<Z_min):
            Z_min=int(Z)
            route_min=list(route)
        
        for i in range(100):
            Tao[route[i]][route[i+1]]+=1/Z
            Tao[route[i+1]][route[i]]+=1/Z
        #Evaporar feromonas
        for i in range(100):
            for j in range(100):
                if(i!=j):
                    Tao[i][j]=(1-ro)*Tao[i][j]
print(Z_min)