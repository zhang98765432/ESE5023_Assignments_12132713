# 张波 地球与空间科学系 物理学 12132713
def Print_values(a,b,c):
    if a>b:
        if b>c :
            print('a,b,c');
        else:
            if a>c:
                print('a,c,b')
            else:
                print('c,a,b');
    else:
        if b>c:
            print('c,a,b');
        else:
            print('c,b,a')
        
import random
#random.randint(1, 100)
#生成1-100之间的随机整数
A=random.randint(1,100)
B=random.randint(1,100)
C=random.randint(1,100)
print(A)
print(B)
print(C)
Print_values(A,B,C)
