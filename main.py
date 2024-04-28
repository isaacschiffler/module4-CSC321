import hashlib
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
from urllib.parse import quote
from Crypto.Util import number
import os

def task1_a(input):
    print("Input text: " + input)
    input_bytes = input.encode('utf-8')
    hash = hashlib.sha256(input_bytes).hexdigest()
    print("Hex Digest of input: 0x" + hash)
    return hash

def task1_b():

    return



if __name__ == '__main__':
    print("---------------------------- Task 1 ----------------------------")
    print("-- a --")
    task1_a("Hello there")
    print("\n-- b --")

