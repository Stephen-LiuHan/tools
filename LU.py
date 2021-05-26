import numpy as np
def LU_decomposition(matA):
    N=len(matA)
    matL = np.zeros(shape=(N,N))
    matU = np.eye(N=N)
    for i in range(N):
        LU = np.zeros(shape=(N,N))
        n = N-i-1 
        l0 = matL[i][i] = matA[0][0]
        l1 = np.zeros(n)
        u1 = np.zeros(n)
        a1 = np.empty((n,n))

        for j in range(n):
            matL[j+i+1][i]=l1[j]=matA[j+1][0]
            matU[i][j+i+1] = u1[j] = matA[0][j+1] / l0
        for j in range(n):
            for k in range(n):
                LU[j][k] = l1[j] * u1[k]
                a1[j][k] = matA[j+1][k+1] - LU[j][k]
        
        matA = a1
        # print(matL)
        # print(matU)
        # print("------------------")

    def solve(b):
        y = np.zeros(N)
        for i in range(N):
            sum = 0
            for j in range(i):
                sum += matL[i][j] * y[j]
            y[i] = (b[i]-sum) / matL[i][i]
        
        x = np.zeros(N)
        for i in range(N-1,0-1,-1):
            sum = 0;
            for j in range(i+1,N):
                sum += matU[i][j] * x[j]
            x[i] = y[i] - sum
        return x
    return solve

if __name__ == '__main__':
    matA = [
        [8, 16, 24,  32],
        [2,  7, 12,  17],
        [6, 17, 32,  59],
        [7, 22, 46, 105]
    ]; 
    b = [
        160, 70, 198, 291,
    ];

    solve = LU_decomposition(matA)
    print(solve(b))
    
    matA = [
        [0, -3,],
        [3,  -7,],
    ]; 
    b = [
        -9, 17,
    ];

    solve = LU_decomposition(matA)

    print(solve(b))