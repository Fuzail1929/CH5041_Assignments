import numpy as np
from math import log,e
import matplotlib.pyplot as plt 

def random(n):
    x0 = 1  
    a = 16807  
    m = (1 << 31) - 1  
    l = []

    for _ in range(n):
        x0 = (a * x0) % m  
        u = x0 /(1.0* m)  
        l.append(u)
    
    return l


def expo_random_numbers(n):
    # lambda parameter is 1
    lambda_parameter=1
    l = random(n)
    ans = [-np.log(i) / lambda_parameter  for i in l]
    return ans
 
    
n=int(input())
res = expo_random_numbers(n)
division = 0.5 # x first belongs to interval [0,division] then [division, 2 * division] and go on


max_i = max(res)
count = [0] * int(max_i/ division + 1)


for i in res:
	i /= division
	count[int(i)]+=1

probability=[]
for i in count:
	probability.append(i/(1.0*n))

lmbda =1 # given 
# we can verify the first element of prob list as 1 - e ** (- lambda * division)

Actual_values = 1 - e ** (-lmbda * division)
Calculated_values = probability[0]

print(f"Real value is {Actual_values} and value obtained is {Calculated_values}")

error = Actual_values - Calculated_values
error_percent = error / Actual_values * 100

print("Error percent is {} %".format(error_percent))

plt.plot(probability) # Now plt refers to matplotlib.pyplot
plt.title("Exponenial distribution")
plt.xlabel("x")
plt.ylabel("Probabilities")
plt.show()
