import numpy as np

def vi_encrypt(Plaintxt,CipherKey):
    if len(CipherKey)<len(Plaintxt):
        l_t = len(Plaintxt)
        l_key = len(CipherKey)
        z = l_t // l_key
        y = l_t % l_key
        CipherKey = iter(CipherKey * z + CipherKey[:y])
    num_key=[ord(i)-ord('a')for i in CipherKey]
    num_txt=[ord(i)-ord('a')for i in txt]
    encrypt_num=(np.array(num_txt)+np.array(num_key))%26
    encrypt=[chr(i+ord('a')) for i in encrypt_num]
    encrypt=''.join(encrypt)
    return encrypt
  

def vi_decrypt(Encrypt, CipherKey):
    if len(CipherKey)<len(Encrypt):
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
