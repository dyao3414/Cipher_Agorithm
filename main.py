from decryption import *
from encryption import *

if __name__ == "__main__":
    plaintxt='ingodwetrust'
    key='zaqwsxcde'
    encrypted_message=encrypt(plaintxt,key)
    print(encrypted_message)
    decrypted_message=decrypt(encrypted_message,key)
    print(decrypted_message)
