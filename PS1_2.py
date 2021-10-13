import random
import numpy as np
# 一般来说，可以使用公式 r = a + (b-a).*rand(N,1) 
# 生成区间 (a,b) 内的 N 个随机数。
M1=np.zeros((5,10))
M2=np.zeros((10,5))
c =np.zeros((5,5))


for j in range(0,10,1):
    for i in range(0,5,1):
        M1[i,j]=random.randint(0,50)
        M2[j,i]=random.randint(0,50)

print(M1)
print(M2)

for i in range(0,5,1):
    for j in range(0,5,1):
        c[i,j]=0
        for k in range(0,5,1):
            c[i,j]= c[i,j]+M1[i,k]*M2[k,j]
#c为M1*M2的结果
print(c)
