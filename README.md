# Hill_Cipher_Agorithm
# Introduction of Hill Cipher


Hill Cipher is a substitution cipher that uses basic matrix theory principles and was invented by Lester S. Hill in 1929. In the cipher algorithm, each letter is reflected to a number modulo 26, for example A=0, B=1, C=2... A string of letters is reflected to a n-dimensional vector, multiplied by an n×n matrix, and then the result is MOD26.

The basic idea of Hill Cipher algorithm is to convert plaintext letters into ciphertext letters through reflection and linear transformation, thus the decryption only needs to do an inverse transformation and inverse reflection, and the key is the transformation matrix itself.
Hill cipher is a type of multi-letter substitution cipher. Multi-letter substitution ciphers can be conveniently described by matrix transformations, so sometimes it's called matrix transformation ciphers.
