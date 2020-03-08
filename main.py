import numpy as np


'''
TODO:create a key generator of desired length
    1. will generate a number as output of fixed length
    2. will change per character in key string
TODO:create a encryption/decryption algo that will use the expanded key and a b;ocl of string as input
    1. create 5 lvl diffusion
    2. easy to compute
    3. block size = ???
'''



data = list(input("enter some text to encrypt"))

key = list(input("enter a key to encrypt"))

def key_gen(initial_pos):
    key_string_length = len(initial_pos)
    for temp1 in range(key_string_length):
        pass
    #return expanded_key







print(data,key)