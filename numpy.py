import numpy as edu
divisor = ("-="*30)

iris_data1 = edu.genfromtxt('iris1.csv',delimiter=',')
iris_data2 = edu.genfromtxt('iris2.csv',delimiter=',')

print(divisor)
print("A quantidade de linhas e colunas é:",iris_data1.shape)
print("A quantidade de linhas e colunas é:",iris_data2.shape)

iris_data = edu.vstack([iris_data1,iris_data2])

print(divisor)
print("A quantidade de linhas e colunas é:",iris_data.shape)

iris_data[~edu.isnan(iris_data).any(axis=1)]

print(divisor)
print("A quantidade de linhas e colunas é:",iris_data.shape)

nodes, counts = edu.unique(iris_data[:,1], return_counts=True)

print(divisor)
print(nodes)
print(counts)

iris_data[:,5][iris_data[:,5] == 0] = 1
iris_data[:,5][iris_data[:,5] == 1] = 2
iris_data[:,5][iris_data[:,5] == 2] = 3

for i in range(3,-1,-1):
    iris_data[:,5][iris_data[:,5] == i] = (i+1)
    caracteristicas = iris_data[:,5:6]
    classes = iris_data[:,5:6]
print(divisor)
print("A quantidade de linhas e colunas é:",caracteristicas.shape)
print("A quantidade de linhas e colunas é:",classes.shape)
edu.savetxt('iris_data_final.csv', iris_data, delimiter=',')