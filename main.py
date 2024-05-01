import hashlib
import bcrypt
from nltk.corpus import words
import time

# Import and download froms from nltk
import nltk
nltk.download('words')

def task1_a(input):
    # print hex digest of a hash of given input
    print("Input text: " + input)
    input_bytes = input.encode('utf-8')
    hash = hashlib.sha256(input_bytes).hexdigest()
    print("Hex Digest of input: 0x" + hash)
    return hash


def task1_b(str1, str2):
    # compare hashes of str1 and str2; Hamming Distance of 1 in this task
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
    messages = {}
    # generate hash for each message in the dictionary
    for j in range(0, (2 ** bits) // 6):
        # calculate the hash for str(j)
        hash_bits = c_helper(str(j), bits)
        if str(hash_bits) in messages:
            # found a collision!
            end_time = time.time()
            print("m0: " + messages[str(hash_bits)])
            print("m1: " + str(j))
            print("hash0: " + str(hash_bits))
            print("hash1: " + str(hash_bits))
            print("COLLISION FOUND!")
            print("Elapsed time: " + str(end_time - start_time) + " seconds\n")
            return
        else:
            messages[str(hash_bits)] = str(j)

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


def task2(bcrypt_hash):
    start_time = time.time()
    # Split the string by $ to get an array of elements
    parts = bcrypt_hash.split('$')

    # Extract the parts
    version = parts[1]
    cost_factor = parts[2]
    salt = parts[3][:22]  # 22 chars for the salt
    real_hash = '$'.join(['', version, cost_factor, salt])
    print(real_hash)

    # Generate a wordlist that contains words between 6 and 10 characters long
    wordlist = [word for word in words.words() if 6 <= len(word) <= 10]

    # Hash each word and check against the provided hash
    for word in wordlist:
        # Use the correct format for bcrypt hash verification
        hashed_word = bcrypt.hashpw(word.encode('utf-8'), real_hash.encode('utf-8'))
        elapsed_time2 = time.time() - start_time
        if hashed_word.decode('utf-8') == bcrypt_hash:
            return word, elapsed_time2

    return None, None


if __name__ == '__main__':
    #t1 = input("Run Task 1? (y/n): ")
    t1 = 'n'  # temp while testing task 2
    if t1 == 'y':
        print("---------------------------- Task 1 ----------------------------")
        print("-- a --")
        task1_a("Hello there")
        print("\n-- b --")
        # each have Hamming Distance of 1
        task1_b("1", "2")
        task1_b("a", "b")
        task1_b("hello", "hellp")
        print("\n-- c --")
        for i in range(8, 51, 2):
            print(str(i) + " bit hash truncation...")
            task1_c(i)
        print("\nDone with task 1c!\n")

    #t2 = input("Run Task 2? (y/n): ")
    t2 = 'y'  # temp while testing task 2
    if t2 == 'y':
        print("---------------------------- Task 2 ----------------------------")
        bcrypt_hash = "$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O"
        password, elapsed_time = task2(bcrypt_hash)
        if password:
            print("Password: " + password)
            print("Elapsed time: " + str(elapsed_time) + " seconds\n")
        else:
            print("Password could not be found.")
