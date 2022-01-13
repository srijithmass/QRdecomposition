''' 
Program to QR decomposition using the Gram-Schmidt method
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
import numpy as np
def qr(A):
    n,m=A.shape
    Q=np.empty((n,n))
    u=np.empty((n,n))
    
    u[:,0]=A[::,0]
    Q[:,0]=u[:,0]/np.linalg.norm(u[:,0])
    
    for i in range (1,n):
        u[:,i]=A[:,i]
        for j in range(i):
            u[:,i]-=(A[:,i]@Q[:,j])*Q[:,j]
            Q[:,i]=u[:,i]/np.linalg.norm(u[:,i])
            
    R = np.zeros((n,m))
    for i in range(n):
        for j in range(i,m):
            R[i,j]=A[:,j]@Q[:,i]
    
    print(Q)
    print(R)
a=np.array(eval(input()))
qr(a)