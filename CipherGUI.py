
from tkinter import *
from tkinter import messagebox
import numpy as np
from sympy import Matrix

alg=0
z=0
def save_hil():
    btn1.config(relief=SUNKEN)
    btn2.config(relief=RAISED)
    btn3.config(relief=RAISED)
    btn4.config(relief=RAISED)
    global alg
    alg=1
    return alg

def save_vi():
    btn1.config(relief=RAISED)
    btn2.config(relief=SUNKEN)
    btn3.config(relief=RAISED)
    btn4.config(relief=RAISED)
    global alg
    alg=2
    return alg


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
    count=0
    while len(plaintxt)%size!=0: #if the lengh of txt cannot be divided by the dimension of ciphermatrix with no remain, add a to the txt
        plaintxt+='a'
        count+=1
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
    return encryptedtxt,count


    
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

def vi_encrypt(Plaintxt,CipherKey):
    l_t = len(Plaintxt)
    l_key = len(CipherKey)
    z = l_t // l_key
    y = l_t % l_key
    CipherKey = iter(CipherKey * z + CipherKey[:y])
    num_key=[ord(i)-ord('a')for i in CipherKey]
    num_txt=[ord(i)-ord('a')for i in Plaintxt]
    encrypt_num=(np.array(num_txt)+np.array(num_key))%26
    encrypt=[chr(i+ord('a')) for i in encrypt_num]
    encrypt=''.join(encrypt)
    return encrypt
    
def vi_decrypt(Encrypt, CipherKey):
    l_t = len(Encrypt)
    l_key = len(CipherKey)
    z = l_t // l_key
    y = l_t % l_key
    CipherKey = iter(CipherKey * z + CipherKey[:y])
    num_key=[ord(i)-ord('a')for i in CipherKey]
    num_encrypt=[ord(i)-ord('a')for i in Encrypt]
    txt_num=(np.array(num_encrypt)-np.array(num_key))%26
    txt=[chr(i+ord('a')) for i in txt_num]
    txt=''.join(txt)
    return txt

def call_encrypt():

    if alg==0:
        messagebox.showinfo("Error",  "Please select a cipher algorithm")
    else:
        Plaintxt = plain.get()
        CipherKey=key.get()
        if Plaintxt=='':
            messagebox.showinfo("Error",  "Please enter plain text")
        elif CipherKey=='':
            messagebox.showinfo("Error",  "Please enter a phrase as cipher key") 
        else:
            if alg==1:
                global z
                x,z=encrypt(Plaintxt,CipherKey)
                out.delete(0,"end")
                out.insert(0, x)
                return z
            elif alg==2:
                x=vi_encrypt(Plaintxt,CipherKey)
                out.delete(0,"end")
                out.insert(0, x)
            
def call_decrypt():        
    print(z)
    if alg==0:
        messagebox.showinfo("Error",  "Please select a cipher algorithm")
    else:
        encryptedtxt = out.get()
        CipherKey=key.get()
        if encryptedtxt=='':
            messagebox.showinfo("Error",  "Please enter encypted text")
        elif CipherKey=='':
            messagebox.showinfo("Error",  "Please enter a phrase as cipher key") 
        else:
            if alg==1:
                x=decrypt(encryptedtxt,CipherKey,z)
                plain.delete(0,"end")
                plain.insert(0, x)
                return
            elif alg==2:
                x=vi_decrypt(encryptedtxt,CipherKey)
                plain.delete(0,"end")
                plain.insert(0, x)
            


def donothing():
    pass

root=Tk()
root.title(string='CIPHER TOOLKIT')

root.eval('tk::PlaceWindow . center')


frame1=Frame(root)
frame1.pack(side=TOP,fill=BOTH)


frametxt=Frame(root)
frametxt.pack(side=TOP,fill=BOTH)

frame2=Frame(root)
frame2.pack(side=TOP, fill=BOTH)
frame3=Frame(root)
frame3.pack(side=TOP, fill=BOTH)
frame4=Frame(root)
frame4.pack(side=TOP, fill=BOTH)
frameopt=Frame(root)
# frameopt.config(=CENTER)
frameopt.pack(anchor = 'center',fill=BOTH)
m=Menu(frame1)
root.config(menu=m)

submenu=Menu(m)
m.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New File', command=donothing)
submenu.add_command(label='Open', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=frame1.quit)


editmenu=Menu(m)
m.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut',command=donothing)
editmenu.add_command(label='Copy',command=donothing)
editmenu.add_command(label='Paste',command=donothing)
editmenu.add_separator()
editmenu.add_command(label='Exit', command=frame1.quit)



toolbar=Frame(frame1,bg='grey')
toolbar.pack(side=TOP,fill=BOTH,anchor = 'center')
toolbar.config(height=20)
btn1=Button(toolbar, text='Hill', command=save_hil)
btn1.config(width=15)
btn2=Button(toolbar, text='Vigenère', command=save_vi)
btn2.config(width=15)
btn3=Button(toolbar, text='N/A', command=donothing)
btn3.config(width=15)
btn4=Button(toolbar, text='N/A', command=donothing)
btn4.config(width=15)
btn1.pack(side=LEFT,anchor = 'e',padx=2)
btn2.pack(side=LEFT,anchor = 'center',padx=2)
btn3.pack(side=LEFT,anchor = 'center',padx=2)
btn4.pack(side=LEFT,anchor = 'e',padx=2)



btnencrypt=Button(frameopt,text='Encrypt',command=call_encrypt)
btnencrypt.config(width=15)
btndecrypt=Button(frameopt,text='Decrypt',command=call_decrypt)
btndecrypt.config(width=15)

btnencrypt.pack(side='left',anchor=E,padx=5,expand=True)
btndecrypt.pack(side='right',anchor=W,padx=5,expand=True)

label=Label(frametxt,text='WELCOME TO CIPHER TOOLKIT',fg='red',bg='white',font=("Arial", 18))
label.config(anchor=CENTER)

label.pack()

label1=Label(frame2,text='Plain Text      ',font=("Arial", 10))
label1.config(anchor=CENTER,height=2)
label2=Label(frame3,text='Key Phrase    ',font=("Arial", 10))
label2.config(anchor=CENTER,height=2)
label3=Label(frame4,text='Encrypted Text',font=("Arial", 10))
label3.config(anchor=CENTER,height=2)

plain=Entry(frame2)
plain.config(width=30)
key=Entry(frame3)
key.config(width=30)
out=Entry(frame4)
out.config(width=30)
label1.pack(side='left')
plain.pack(side='left',fill="none",expand=True)
label2.pack(side='left')
key.pack(side='left',fill="none",expand=True)
label3.pack(side='left')
out.pack(side='left',fill="none",expand=True)






status= Label(root,text='version 0.1.0   author Di Yao',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
