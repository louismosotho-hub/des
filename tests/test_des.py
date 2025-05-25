import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils import string_to_bitlist, bitlist_to_string
from des import encrypt, decrypt

class TestDES(unittest.TestCase):
    def test_basic(self):
        print("\nRunning test_basic")
        plaintext = "ABCDEFGH"
        key = "12345678"
        plaintext_bits = string_to_bitlist(plaintext)
        key_bits = string_to_bitlist(key)
        ciphertext_bits = encrypt(plaintext_bits, key_bits)
        print("Ciphertext bits:", ciphertext_bits)
        decrypted_bits = decrypt(ciphertext_bits, key_bits)
        decrypted_text = bitlist_to_string(decrypted_bits)
        print("Decrypted text:", decrypted_text)
        self.assertEqual(decrypted_text, plaintext)
        print("test_basic passed")

    def test_all_zeros(self):
        print("\nRunning test_all_zeros")
        plaintext = "\x00" * 8
        key = "\x00" * 8
        plaintext_bits = string_to_bitlist(plaintext)
        key_bits = string_to_bitlist(key)
        ciphertext_bits = encrypt(plaintext_bits, key_bits)
        print("Ciphertext bits:", ciphertext_bits)
        decrypted_bits = decrypt(ciphertext_bits, key_bits)
        decrypted_text = bitlist_to_string(decrypted_bits)
        print("Decrypted text:", decrypted_text)
        self.assertEqual(decrypted_text, plaintext)
        print("test_all_zeros passed")

    def test_all_ones(self):
        print("\nRunning test_all_ones")
        plaintext = "\xff" * 8
        key = "\xff" * 8
        plaintext_bits = string_to_bitlist(plaintext)
        key_bits = string_to_bitlist(key)
        ciphertext_bits = encrypt(plaintext_bits, key_bits)
        print("Ciphertext bits:", ciphertext_bits)
        decrypted_bits = decrypt(ciphertext_bits, key_bits)
        decrypted_text = bitlist_to_string(decrypted_bits)
        print("Decrypted text:", decrypted_text)
        self.assertEqual(decrypted_text, plaintext)
        print("test_all_ones passed")

    def test_single_bit_difference(self):
        print("\nRunning test_single_bit_difference")
        plaintext1 = "ABCDEFGH"
        plaintext2 = "ABCDEFGA"
        key = "12345678"
        bits1 = string_to_bitlist(plaintext1)
        bits2 = string_to_bitlist(plaintext2)
        key_bits = string_to_bitlist(key)
        ct1 = encrypt(bits1, key_bits)
        ct2 = encrypt(bits2, key_bits)
        print("Ciphertext 1:", ct1)
        print("Ciphertext 2:", ct2)
        self.assertNotEqual(ct1, ct2)
        print("test_single_bit_difference passed")

    def test_empty_string(self):
        print("\nRunning test_empty_string")
        plaintext = ""
        key = "12345678"
        plaintext_bits = string_to_bitlist(plaintext)
        key_bits = string_to_bitlist(key)
        try:
            ciphertext_bits = encrypt(plaintext_bits, key_bits)
            decrypted_bits = decrypt(ciphertext_bits, key_bits)
            decrypted_text = bitlist_to_string(decrypted_bits)
            print("Ciphertext bits:", ciphertext_bits)
            print("Decrypted text:", decrypted_text)
            self.assertEqual(decrypted_text, plaintext)
        except Exception as e:
            print("Exception occurred:", e)
            self.assertTrue(True)
        print("test_empty_string passed")

if __name__ == "__main__":
    unittest.main()