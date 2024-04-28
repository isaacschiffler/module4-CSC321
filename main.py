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

def task1_b(str1, str2):
    print("Hash " + str1 + " vs. " + str2)
    input_bytes = str1.encode('utf-8')
    hash1 = hashlib.sha256(input_bytes).hexdigest()
    input_bytes = str2.encode('utf-8')
    hash2 = hashlib.sha256(input_bytes).hexdigest()
    print("Hash1: 0x" + hash1)
    print("Hash2: 0x" + hash2)
    return



if __name__ == '__main__':
    print("---------------------------- Task 1 ----------------------------")
    print("-- a --")
    task1_a("Hello there")
    print("\n-- b --")
    task1_b("1", "2")
    task1_b("a", "b")
    task1_b("hello", "hellp")
    print("\n-- c --")


