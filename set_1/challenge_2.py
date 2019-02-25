from base64 import b64encode
from codecs import decode, encode

#Takes two hex strings and applys an xor
def apply_xor(input_string,xor_string):
    input_string_array = bytearray.fromhex(input_string)
    xor_string_array = bytearray.fromhex(xor_string)
    byte_array = bytearray(len(input_string))

    for i in range(len(input_string_array)):
        byte_array[i] = input_string_array[i] ^ xor_string_array[1]
    return byte_array


def decode_string(input_string):
    hex_string = decode(input_string, "hex")
    return hex_string

starting_string = "1c0111001f010100061a024b53535009181c"
xor_string = "686974207468652062756c6c277320657965"
expected_string = "746865206b696420646f6e277420706c6179"

hex_string = decode_string(starting_string)
print(type(hex_string))
hex_xor_string = decode_string(xor_string)
#xor_string = apply_xor(hex_string,hex_xor_string)
xor_string = apply_xor(starting_string,xor_string)

print encode(bytes(xor_string),"hex")