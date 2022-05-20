# Cipher_Agorithm

This repository is still being written, as many functions are not complete yet.

### CipherGUI.py

This file is intended to be an integration of all the cipher methods in this repository, and it provides a user interface for easy use. The GUI interface is entirely written in python by TKinter library.




![1653016658(1)](https://user-images.githubusercontent.com/102843970/169443592-4d4d2f16-efda-464c-ab31-8dc7b635cee2.png)

When encrypting, simply select the method you want to use. After clicking, the button selected will be sunkun, as it tells you the cipher method is being used.
The plain text field is to enter the text that you want to be ciphered, the Key phrase field is for Cipher key entry

Let's try a really cool example！
For example, I selected the Hill cipher as my method to encrypt, and I entered text that I wanted to cipher "Attack is tonight please do it quick"
Note, there will be no space when I type that in
And my key phrase is "thereisnofreelan"
Note, for Hill Cipher, the length of key phrase needs to be a perfect square number, such as 9, 16, 25 etc. Because the concept of Hill Cipher is to convert key phrase to a sqaured matrix.
Now, my interface looks like this
![1662d79e2b2dab2567b966eb746febd](https://user-images.githubusercontent.com/102843970/169444458-88d2524e-642a-422e-826d-ef33b8257fa7.png)

When I hit encrypt, the encrupted message is shown in the Encrypted Text field 

![1653017227(1)](https://user-images.githubusercontent.com/102843970/169444656-002e5e50-e7f6-45dc-8f3d-1f76944f4f59.png)


Thus "gtmeafdlzayyyuuyuavoegdvaylgyvbh" is my encrypted message.




### Introduction of Hill Cipher


Hill Cipher is a substitution cipher that uses basic matrix theory principles and was invented by Lester S. Hill in 1929. In the cipher algorithm, each letter is reflected to a number modulo 26, for example A=0, B=1, C=2... A string of letters is reflected to a n-dimensional vector, multiplied by an n×n matrix, and then the result is MOD26.

The basic idea of Hill Cipher algorithm is to convert plaintext letters into ciphertext letters through reflection and linear transformation, thus the decryption only needs to do an inverse transformation and inverse reflection, and the key is the transformation matrix itself.
Hill cipher is a type of multi-letter substitution cipher. Multi-letter substitution ciphers can be conveniently described by matrix transformations, so sometimes it's called matrix transformation ciphers.

It is not difficult to see that there are two very important conditions in the Hill cipher algorithm. The first condition is the correspondence table between characters (information) and numbers. When the order n of the encryption matrix is larger, the difficulty of deciphering will increase, and the amount of calculation will also be larger. The second condition is the encryption matrix. How to define and solve this matrix is very important for encryption and decryption of passwords.

The traditional way of cipher has a fatal weakness, that is, the decipherers can find the pattern from the frequency of the characters, and then find the breakthrough of deciphering, especially with today's highly developed computer technology, the deciphering speed has dramatically increased. The Hill cipher algorithm completely overcomes this defect. By using the matrix multiplication and inverse operations in linear algebra, Hill cipher can better resist frequency analysis and is difficult to break from this angle.

The Hill cipher system sets up at least three barriers for decipherers, which increases the difficulty of deciphering. The key to deciphering the Hill cipher is to guess how the text is converted into a few-dimensional vector, how the corresponding alphabet is arranged, and more importantly, is to obtain the encrypted matrix. To crack the password, the dimension of the vector, the permutation table of the letters and the encryption matrix are indispensable 
