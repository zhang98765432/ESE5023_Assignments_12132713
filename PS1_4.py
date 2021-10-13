import random
import math
a=random.randint(1,100)

step=0
print(a)
while a>1:
    if  math.fmod(a,2)==0:
        step=step+1
        a=a/2
    else:
        step=step+1
        a=(a-1)/2
        step=step+1
# step就是最后的总步数
print(step)
