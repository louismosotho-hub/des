PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute(key, table):
    result = []
    for i in table:
        result.append(key[i - 1])
    return result

def left_shift(bits, shifts):
    shifted = []
    for i in range(len(bits)):
        shifted_index = (i + shifts) % len(bits)
        shifted.append(bits[shifted_index])
    return shifted

def generate_round_keys(key):
    permuted_key = permute(key, PC1)
    
    left = permuted_key[:28]
    right = permuted_key[28:]
    
    round_keys = []
    
    for shifts in SHIFT_SCHEDULE:
        left = left_shift(left, shifts)
        right = left_shift(right, shifts)

        combined_key = left + right
        round_key = permute(combined_key, PC2)
        round_keys.append(round_key)
    
    return round_keys