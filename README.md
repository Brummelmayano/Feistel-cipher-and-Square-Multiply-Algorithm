# Feistel Cipher and Square & Multiply Algorithm

This repository provides a complete implementation of the Feistel Cipher and the Square & Multiply Algorithm in Python. These cryptographic algorithms are widely used for secure communication and modular exponentiation, respectively.

A heartfelt thank you to Junior Kaningini and Professor Pierre Kasengedia

## Feistel Cipher

The Feistel Cipher is a symmetric-key encryption algorithm that divides the input into blocks and applies multiple rounds of processing to achieve encryption and decryption. The key features include customizable key generation, permutation functions, and shift orders.

### Usage:

1. **Run the Algorithm:**
   - Execute the `main.py` script to test the Feistel Cipher implementation.

2. **Input Instructions:**
   - When prompted, enter the key (8 bits) and the message block (8 bits) for encryption.
   - Optionally, customize the algorithm by specifying permutations and shift orders or proceed with default values.

3. **Output Display:**
   - The script will display the original message block, the encrypted ciphertext, and the decrypted message block.

## Square & Multiply Algorithm

The Square & Multiply Algorithm is commonly used for efficient modular exponentiation, a crucial operation in many cryptographic protocols. This algorithm significantly reduces the number of computations compared to straightforward exponentiation.

### Usage:

1. **Run the Algorithm:**
   - Execute the `main.py` script and choose option 2 to test the Square & Multiply Algorithm.

2. **Input Instructions:**
   - Enter the base (`x`), exponent (`b`), and modulus (`n`) values.

3. **Output Display:**
   - The script will calculate and display the result of `x^b (mod n)` using the Square & Multiply Algorithm.


Your feedback and contributions are welcome!

