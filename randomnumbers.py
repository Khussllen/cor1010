#random numbers 

import random
import numpy as np

number= random.randint(1, 100)
print(number)

for row in range(10):

    for j in range(row):
        print(" ",end=" ")

    for j in range(10-row):
        print(j,end=" ")
    print()

listOfRandomNumbers= []
for i in range(100):
    n=random.randint(1, 20)
    listOfRandomNumbers.append(n)

print(listOfRandomNumbers)

list2= [random.randint(1, 20) for in range(100)]
print(list2)
print("length of list2 is ")


total=0
for number in listOfRandomNumbers:
    total= total + number
print("total: ", total)
