from codecs import decode, encode
from Crypto.Util.strxor import strxor_c

# Takes two hex strings and applys an xor
def apply_xor(input_string,xor_string):
    # bytes is iterable so zip down the two iterables and apply the xor
    return bytes(x ^ y for x, y in zip(input_string, xor_string))


def decode_string(input_string):
    hex_string = decode(input_string, "hex")
    return hex_string


# Letter frequency courtesy of http://norvig.com/mayzner.html
freqs = {
    'a': 0.0804,
    'b': 0.0148,
    'c': 0.0334,
    'd': 0.0382,
    'e': 0.1249,
    'f': 0.0240,
    'g': 0.0187,
    'h': 0.0505,
    'i': 0.0757,
    'j': 0.0016,
    'k': 0.0054,
    'l': 0.0407,
    'm': 0.0251,
    'n': 0.0723,
    'o': 0.0764,
    'p': 0.0214,
    'q': 0.0012,
    'r': 0.0628,
    's': 0.0654,
    't': 0.0928,
    'u': 0.0273,
    'v': 0.0105,
    'w': 0.0168,
    'x': 0.0023,
    'y': 0.0166,
    'z': 0.0009,
    ' ': 0.1354
}

# For each character in string, look up value in freqs and add it together
def score_result(s):
    score = 0
    for i in s:
        char = chr(i).lower()
        if char in freqs:
            score += freqs[char]
    return score


# This string has been xor'd against a single character find the key
starting_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
starting_string = decode_string(starting_string)

results = []
# For each character in english language (ascii)
for i in range(255):
    xor_applied_string = strxor_c(starting_string, i)
    scored_sentence = score_result(xor_applied_string)
    results.append({"score": scored_sentence, "xor_string": xor_applied_string.decode("ascii", errors="ignore")})

max_score = 0
max_sentence = ""

for item in results:
    # print(item)
    if item["score"] > max_score:
        max_score = item["score"]
        max_sentence = item["xor_string"]


print(max_score)
print(max_sentence)
