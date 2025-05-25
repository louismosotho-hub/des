# DES CLI

This project is a simple implementation of the DES (Data Encryption Standard) symmetric cipher in Python.

## Features

- Symmetric encryption and decryption using DES.
- Support for 64-bit block size and 56-bit key size.
- Implementation of all DES operations: initial permutation, key schedule, Feistel rounds, and final permutation.
- Command-line interface (CLI) for encrypting and decrypting 8-character blocks.
- Unit tests for correctness.

## Usage

### CLI

Run the CLI from the project directory:

```bash
python3 des_cli.py
```

You will be prompted to choose a mode (`encrypt` or `decrypt`), enter an 8-character text or ciphertext, and an 8-character key.

- **Encryption:**  
  - Enter your plaintext (8 characters) and key (8 characters).
  - The CLI will output the ciphertext in hexadecimal (safe for copy-paste).

- **Decryption:**  
  - Enter the ciphertext as 16 hex digits (from the encryption output) or as 8 characters.
  - Enter the same key used for encryption.
  - The CLI will output the original plaintext.

#### Example

```
DES Cipher CLI
--------------
Enter mode (encrypt/decrypt): encrypt
Enter text (8 characters): Louis008
Enter key (8 characters): testkey1
Ciphertext (hex): 5b60f22bf0a62509

DES Cipher CLI
--------------
Enter mode (decrypt)
Enter ciphertext (8 characters or 16 hex digits): 5b60f22bf0a62509
Enter key (8 characters): testkey1
Plaintext: Louis008
```

## Testing

Run the test suite to verify the implementation:
```bash
python3 tests/test_des.py
```

## Notes

- **DES operates on 8-byte (64-bit) blocks and 8-byte keys.**  
  Both plaintext and key must be exactly 8 characters.
- Ciphertext is shown in hexadecimal for safe copy-paste and reversibility.
