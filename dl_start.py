print("Hello World! \n")
print("Initialize DL Course \n")


#Basic python functions
#Printing random numbers
import random 

x = [random.randint(0,100) for i in range(10)]
print(x)
print("Min", min(x)) 
print("Max", max(x))

x.sort()
print("Sorted", x)

#Data type casting
y = [random.random()*100 for i in range(10)]
print(y)

y = [int(i) for i in y ]
print(y)

## Numpy

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)

a.dtype
a.shape