import numpy as np
from sympy import Matrix

def encrypt(plaintxt,cipherKey):
    size=int(np.sqrt(len(cipherKey)))
    if size*size!=len(cipherKey):
        print('Error,the length of cipher key needs to be a percfect square number')
        return
    lst=[cipherKey[i:i+size].lower()for i in range(0, len(cipherKey), size)]
    ciphermatrix=[]
    for i in range(0,len(lst)):
        temp=[ord(letter)-ord('a')for letter in list(lst[i])]
        ciphermatrix.append((temp))
    ciphermatrix=np.mat(ciphermatrix)
    if np.linalg.det(ciphermatrix)==0:
        print('error the ciphermatrix is not invertable')
        return
    try:
        inv_cipher=np.mat(Matrix(ciphermatrix).inv_mod(26)) #test if the matrix is invertable
    except:
        print('the cipherKey matrix is not invertable')
        return
    while len(plaintxt)%size!=0: #if the lengh of txt cannot be divided by the dimension of ciphermatrix with no remain, add a to the txt
        plaintxt+='a'
    col_dim=int(len(plaintxt)/size) # calculate how many columns the txt_matrix is
    lst=[plaintxt[i:i+col_dim].lower()for i in range(0, len(plaintxt), col_dim)]
    txtmatrix=[]
    for i in range(0,len(lst)):
        temp=[ord(letter)-ord('a')for letter in list(lst[i])]
        txtmatrix.append((temp))
    txtmatrix=np.mat(txtmatrix)
    encrypt_matrix=np.matmul(ciphermatrix,txtmatrix)%26
    row,col=encrypt_matrix.shape
    encryptedtxt=''
    for i in range(0,row):
        for j in range(0,col):
            encryptedtxt+=chr(encrypt_matrix[i,j]+ord('a'))
    return encryptedtxt