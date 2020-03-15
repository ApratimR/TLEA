'''
TODO:create a key generator of desired length
    1. will generate a number as output of fixed length
    2. will change per character in key string
TODO:create a encryption/decryption algo that will use the expanded key and a b;ocl of string as input
    1. create 5 lvl diffusion
    2. easy to compute
    3. block size = ???
'''

import numpy as np

def converter(parameter1):
    local_ar1 = []
    for temp1 in parameter1:
        local_ar1.append(ord(temp1))
    return local_ar1

data = list(input("enter some text to encrypt"))

key = converter(list(input("enter a key to encrypt")))



def key_gen(key):
    key_string_length = len(key)
    for temp1 in range(key_string_length):
        pass
    #return expanded_key