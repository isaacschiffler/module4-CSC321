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
import random
import time


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


def task1_c(bits):
    # get start time
    start_time = time.time()
    # create the message dictionary
    messages = message_gen(bits)
    # generate hash for each message in the dictionary
    for key in messages.keys():
        # assign hash to key in dictionary
        messages[key] = c_helper(key, bits)

    for key1 in messages.keys():
        for key2 in messages.keys():
            if messages[key1] == messages[key2] and key1 != key2:
                # get collision time
                end_time = time.time()
                print("m0: " + key1)
                print("m1: " + key2)
                print("hash0: " + str(messages[key1]))
                print("hash1: " + str(messages[key2]))
                print("COLLISION FOUND!")
                print("Elapsed time: " + str(end_time - start_time) + " seconds\n")
                return

    end_time = time.time()
    print("No collision found in " + str(end_time - start_time) + " seconds")
    return


def c_helper(input, size: int):
    # function to get the truncated binary hash given the size requested
    input_bytes = input.encode('utf-8')
    hash_digest = hashlib.sha256(input_bytes).digest()
    binary_hash = ''.join(format(byte, '08b') for byte in hash_digest) # format binary
    hash_trunc = binary_hash[:size] # get up to [size] bits
    return hash_trunc


def message_gen(bits):
    dict = {}
    for i in range(0, (2 ** bits) // 8):
        dict[str(i)] = 0
    return dict



if __name__ == '__main__':
    print("---------------------------- Task 1 ----------------------------")
    print("-- a --")
    task1_a("Hello there")
    print("\n-- b --")
    task1_b("1", "2")
    task1_b("a", "b")
    task1_b("hello", "hellp")
    print("\n-- c --")
    for i in range(8, 51, 2):
        print(str(i) + " bit hash truncation...")
        task1_c(i)
    print("\nDone with task 1c!")

