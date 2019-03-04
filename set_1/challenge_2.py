from codecs import decode, encode


# Takes two hex strings and applys an xor
def apply_xor(input_string,xor_string):
    # bytes is iterable so zip down the two iterables and apply the xor
    return bytes(x ^ y for x, y in zip(input_string, xor_string))


def decode_string(input_string):
    hex_string = decode(input_string, "hex")
    return hex_string

starting_string = "1c0111001f010100061a024b53535009181c"
xor_string = "686974207468652062756c6c277320657965"
expected_string = b"746865206b696420646f6e277420706c6179"

hex_string = decode_string(starting_string)
hex_xor_string = decode_string(xor_string)
xor_string = apply_xor(hex_string,hex_xor_string)
xor_string = encode(xor_string, "hex")

if xor_string == expected_string:
    print("String Matched Expected String")
else:
    print("Strings did not match: Got {}, Expected: {}".format(xor_string,expected_string))
