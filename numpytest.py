import numpy as np

print(' my numpy version: ', np.__version__)

n=np.random.randint(1, 20)
randomList=[]
for i in range(100):
    n=np.random.randint(1, 20)
    randomList.append(n)
#
print("randomLsit:", randomList)
