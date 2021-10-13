def Pascal_triangle(N):
    #li = [0 for i in range((N**2))]
    import numpy as np
    arr = np.eye(N, N, dtype=int)
    for i in range(N):
        arr[i][0] = 1
    for i in range(1, N):
        for j in range(N):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
   
    # 打印全部的arr和打印arr的最后一行
    #print(arr)  
    print(arr[i,:])


Pascal_triangle(100)

Pascal_triangle(200)