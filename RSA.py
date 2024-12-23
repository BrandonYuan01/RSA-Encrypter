import random
import math


def isPrime(n):
    if n == 1:  # base case
        return True
    for i in range(2, (n // 2) + 1):
        if (n % i) == 0:
            return False
    return True


def generatePQ():
    while True:
        p = random.randint(10, 1000000)  # generate random values for p and q
        q = random.randint(10, 1000000)
        if isPrime(p) and isPrime(q) and p != q:  # once they're both prime and they dont equal each other return
            return p, q


def generateE(phi):
    while 1:
        e = random.randint(2, phi)  # create a random e
        if math.gcd(e, phi) == 1 and e < phi:  # check if e is coprime and less than phi
            return e


# p = 349207  # test stuff
# q = 966209
# e = 69759637427
# p, q = 11, 13

p, q = generatePQ()  # call generatePQ to find primes for p and q
n = p*q
phi = (p-1) * (q-1)
e = generateE(phi)  # generate an e value
d = pow(e, -1, phi)  # calculate private key

message = input("Enter message: ")  # ask user for message to encrypt
encrypted_message = ciphertext = [pow(ord(char), e, n) for char in message]  # list of encrypted characters from message
decrypted_message = ''.join([chr(pow(cipher, d, n)) for cipher in ciphertext])  # create string of decrypted cipher
print("p: " + str(p))
print("q: " + str(q))
print("e: " + str(e))
print("d: " + str(d))
print("Ciphertext: " + str(encrypted_message))
print("Decrypted message: " + str(decrypted_message))
