from core import initial_permutation, final_permutation, feistel_function
from key_schedule import generate_round_keys

def encrypt(plaintext, key):
    bits = initial_permutation(plaintext)

    left = bits[:32]
    right = bits[32:]

    round_keys = generate_round_keys(key)

    for i in range(16):
        temp = right.copy()
        f_out = feistel_function(right, round_keys[i])
        right = [l ^ f for l, f in zip(left, f_out)]
        left = temp

    combined = right + left

    ciphertext = final_permutation(combined)
    return ciphertext

def decrypt(ciphertext, key):
    bits = initial_permutation(ciphertext)

    left = bits[:32]
    right = bits[32:]

    round_keys = generate_round_keys(key)

    for i in range(16):
        temp = right.copy()
        f_out = feistel_function(right, round_keys[15 - i])
        right = [l ^ f for l, f in zip(left, f_out)]
        left = temp

    combined = right + left

    plaintext = final_permutation(combined)
    return plaintext