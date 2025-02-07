import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import random

# Initialize x0 globally
x0 = 1

def rand_uniform():
    global x0
    a = 16807
    m = (1 << 31) - 1
    x0 = (a * x0) % m
    return (x0 / m)  

def distance(x, y):
    return x * x + y * y


# no of steps in each walk
n = 10000

# no of different walks
m=5

delta = 0.01 
walks_x_coordinate = []
walks_y_coordinate = []

for i in range(m):
    arr_x = [0]
    arr_y = [0]
    for j in range(n):
        x = rand_uniform()
        y = rand_uniform()
        if(x>=0.5) :
          arr_x.append(arr_x[-1] + delta)
        else :
          arr_x.append(arr_x[-1] - delta)
        if(y>=0.5) :
          arr_y.append(arr_y[-1] + delta)
        else :
          arr_y.append(arr_y[-1] - delta)


    walks_x_coordinate.append(arr_x)
    walks_y_coordinate.append(arr_y)

# Plot random walks
for i in range(m):
    plt.plot(walks_x_coordinate[i], walks_y_coordinate[i])
plt.title(f"Plot 1: {m} Random Walks")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.show()


                     # QUESTION 4 USING THE FIRST RANDOM TRAJECTORY FROM PREVIOUS Question

# Using the first random trajectory
X = walks_x_coordinate[0]
Y = walks_y_coordinate[0]

DeltaT = [1, 5, 10, 20, 100, 200, 400, 800, 1000, 2000, 4000, 8000]

# mean square difereence array MSU[i]= (x-xmean)**2 +(y-ymean)**2
MSU = []
for i in DeltaT:
    msq = []
    for j in range(0, n - i):
        msq.append(distance(X[j + i] - X[j], Y[j + i] - Y[j]))
    MSU.append(sum(msq) / len(msq))

DeltaT = np.array(DeltaT)
MSU = np.array(MSU)

slope, intercept, _, _, _ = linregress(np.log(DeltaT), np.log(MSU))
print(f"Slope: {slope}, Intercept: {intercept}")
# ln MSU = ln(4*D)+ln(t)
# D is e^(intercept value from graph)/4
D = np.exp(intercept)/4
print(f"Value of D is {D} ")

plt.scatter(np.log(DeltaT),np.log(MSU), label="Data")
plt.plot(np.log(DeltaT), slope*np.log(DeltaT) + intercept, color='green', label="Linear Fit")
plt.title("Plot 2: Msq vs Delta T")
plt.xlabel("ln(Delta T)")
plt.ylabel("ln(Mean_Square)")
plt.legend()
plt.show()



