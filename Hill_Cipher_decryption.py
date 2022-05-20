import numpy as np
from sympy import Matrix

def decrypt(encryptedtxt,cipherKey,count=0):
    size=int(np.sqrt(len(cipherKey)))
    if size*size!=len(cipherKey):
        print('Error,the length of cipher key needs to be a percfect square number')
        return
    lst=[cipherKey[i:i+size] for i in range(0, len(cipherKey), size)]
    ciphermatrix=[]
    for i in range(0,len(lst)):
        temp=[ord(letter)-ord('a')for letter in list(lst[i])]
        ciphermatrix.append((temp))
    ciphermatrix=np.mat(ciphermatrix)
    inv_cipher=np.mat(Matrix(ciphermatrix).inv_mod(26))
    col_dim=int(len(encryptedtxt)/size) # calculate how many columns the txt_matrix is
    lst=[encryptedtxt[i:i+col_dim].lower()for i in range(0, len(encryptedtxt), col_dim)]
    encrypt_txt_matrix=[]
    for i in range(0,len(lst)):
        temp=[ord(letter)-ord('a')for letter in list(lst[i])]
        encrypt_txt_matrix.append((temp))
    encrypt_txt_matrix=np.mat(encrypt_txt_matrix)
    txt_matrix=inv_cipher@encrypt_txt_matrix%26
    row,col=txt_matrix.shape
    plaintxt=''
    for i in range(0,row):
        for j in range(0,col):
            plaintxt+=chr(int(txt_matrix[i,j]+ord('a')))
    if count !=0:
      plaintxt=plaintxt[0:-(count)]
    return plaintxt
