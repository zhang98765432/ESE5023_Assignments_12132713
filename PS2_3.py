#第一个模块
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('F:\JuneGH.xlsx')
print(data)

#第二个模块
data.sort_values("GH")

#第san个模块
df=pd.DataFrame(data)
x=df.iloc[:,0].values
y=df.iloc[:,1].values
plt.figure(num=3)
plt.bar(x,y)
plt.plot(x,y,color='red')
plt.xlabel('time')
plt.ylabel('GH')
plt.show()

#第四个模块
data.describe()