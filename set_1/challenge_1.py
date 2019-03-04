import base64
from codecs import decode

starting_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected_string = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

#Decode the hex to ascii byte array
hex_string = decode(starting_string, 'hex')
#pass byte array to b64encode
encoded_string = base64.b64encode(hex_string)

print(hex_string)
print(encoded_string)

if encoded_string != expected_string:
    raise Exception("Encoded value did not work as expected")
print(encoded_string)
