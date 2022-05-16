# Hill_Cipher_Agorithm
### Introduction of Hill Cipher


Hill Cipher is a substitution cipher that uses basic matrix theory principles and was invented by Lester S. Hill in 1929. In the cipher algorithm, each letter is reflected to a number modulo 26, for example A=0, B=1, C=2... A string of letters is reflected to a n-dimensional vector, multiplied by an n×n matrix, and then the result is MOD26.

The basic idea of Hill Cipher algorithm is to convert plaintext letters into ciphertext letters through reflection and linear transformation, thus the decryption only needs to do an inverse transformation and inverse reflection, and the key is the transformation matrix itself.
Hill cipher is a type of multi-letter substitution cipher. Multi-letter substitution ciphers can be conveniently described by matrix transformations, so sometimes it's called matrix transformation ciphers.

It is not difficult to see that there are two very important conditions in the Hill cipher algorithm. The first condition is the correspondence table between characters (information) and numbers. When the order n of the encryption matrix is larger, the difficulty of deciphering will increase, and the amount of calculation will also be larger. The second condition is the encryption matrix. How to define and solve this matrix is very important for encryption and decryption of passwords.

The traditional way of cipher has a fatal weakness, that is, the decipherers can find the pattern from the frequency of the characters, and then find the breakthrough of deciphering, especially with today's highly developed computer technology, the deciphering speed has dramatically increased. The Hill cipher algorithm completely overcomes this defect. By using the matrix multiplication and inverse operations in linear algebra, Hill cipher can better resist frequency analysis and is difficult to break from this angle.

The Hill cipher system sets up at least three barriers for decipherers, which increases the difficulty of deciphering. The key to deciphering the Hill cipher is to guess how the text is converted into a few-dimensional vector, how the corresponding alphabet is arranged, and more importantly, is to obtain the encrypted matrix. To crack the password, the dimension of the vector, the permutation table of the letters and the encryption matrix are indispensable 
