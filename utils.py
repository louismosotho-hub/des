def string_to_bitlist(data):
    bits = []
    for char in data:
        ascii_value = ord(char)
        bin_str = format(ascii_value, '08b')
        for bit in bin_str:
            bits.append(int(bit))
    return bits

def bitlist_to_string(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_str = ''
        for b in byte:
            byte_str += str(b)
        ascii_value = int(byte_str, 2)
        char = chr(ascii_value)
        chars.append(char)
    result = ''
    for c in chars:
        result += c
    return result
