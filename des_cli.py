from utils import string_to_bitlist, bitlist_to_string
from des import encrypt, decrypt

def bits_to_bytes(bits):
    # Convert a list of bits to bytes (8 bits per byte)
    byte_list = []
    for i in range(0, 64, 8):
        byte_str = ''
        for bit in bits[i:i+8]:
            byte_str += str(bit)
        byte_value = int(byte_str, 2)
        byte_list.append(byte_value)
    return bytes(byte_list)

def bytes_to_bits(byte_data):
    # Convert bytes to a list of bits
    bits = []
    for byte in byte_data:
        bin_str = format(byte, '08b')
        for bit in bin_str:
            bits.append(int(bit))
    return bits

def main():
    print("DES Cipher CLI")
    print("--------------")
    mode = input("Enter mode (encrypt/decrypt): ")
    mode = mode.strip().lower()

    if mode == "encrypt":
        text = input("Enter text (8 characters): ")
        text = text.strip()
        key = input("Enter key (8 characters): ")
        key = key.strip()

        if len(text) != 8:
            print("Text must be exactly 8 characters long for encryption.")
            return

        if len(key) != 8:
            print("Key must be exactly 8 characters long.")
            return

        # Convert text and key to bitlists
        text_bits = string_to_bitlist(text)
        key_bits = string_to_bitlist(key)

        # Encrypt the text
        ciphertext_bits = encrypt(text_bits, key_bits)

        # Convert ciphertext bits to a string for display (uncomment for raw output testing)
        # ciphertext = bitlist_to_string(ciphertext_bits)
        # print("Ciphertext:", ciphertext)

        # Convert ciphertext bits to bytes and hex for display
        ciphertext_bytes = bits_to_bytes(ciphertext_bits)
        ciphertext_hex = ciphertext_bytes.hex()

        print("Ciphertext (hex):", ciphertext_hex)

    elif mode == "decrypt":
        text = input("Enter ciphertext (8 characters or 16 hex digits): ")
        text = text.strip()
        key = input("Enter key (8 characters): ")
        key = key.strip()

        if len(key) != 8:
            print("Key must be exactly 8 characters long.")
            return

        key_bits = string_to_bitlist(key)

        # Detect if input is hex or raw string
        if len(text) == 16:
            try:
                ciphertext_bytes = bytes.fromhex(text)
                ciphertext_bits = bytes_to_bits(ciphertext_bytes)
            except ValueError:
                print("Invalid hex input for ciphertext.")
                return
        elif len(text) == 8:
            ciphertext_bits = string_to_bitlist(text)
        else:
            print("Ciphertext must be exactly 8 characters or 16 hex digits long for decryption.")
            return

        # Decrypt the ciphertext
        plaintext_bits = decrypt(ciphertext_bits, key_bits)
        plaintext = bitlist_to_string(plaintext_bits)
        print("Plaintext:", plaintext)

    else:
        print("Unknown mode. Please use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()