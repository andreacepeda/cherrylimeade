import random
from prettytable import PrettyTable

def random_cjk(length=10):
    return ''.join(chr(random.randint(0x4E00, 0x9FFF)) for _ in range(length))
cjk_string = random_cjk()

print(f"CJK Charecters Encoded: {random_cjk()} Length: {len(random_cjk())}")

encoding_schemes = ['ascii', 'latin-1', 'cp1252', 'utf-8', 'utf-16', 'utf-32']
results = []
def encode_string(cjk_string):
    encoded_data = {}
    for encoding in encoding_schemes:
        try:
            encoded_data[encoding] = cjk_string.encode(encoding)
            results.append([encoding, None, None, None, None, None, None])
        except Exception as e:
            results.append([encoding, None, None, None, None, None, str(e)])
            encoded_data[encoding] = None
    return encoded_data

def decode_string(encoded_data):
    for write_encoding, data in encoded_data.items():
        if data is None:
            continue
        for read_encoding in encoding_schemes:
            try:
                decoded_data = data.decode(read_encoding)
                
                char_length = len(decoded_data)
                byte_length = len(data)
                hex_version = data.hex()
                
                results.append([write_encoding, read_encoding, decoded_data, char_length, byte_length, hex_version, None])
            except Exception as e:
                results.append([write_encoding, read_encoding, None, None, None, None, str(e)])

encoded_data = encode_string(cjk_string)
decode_string(encoded_data)

table = PrettyTable()
table.field_names = ["Wencode", "Rencode", "CharLen", "BytesLen", "DecodedChars", "HexString", "Error"]

for row in results:
    table.add_row(row)

table.border = False
table.align = "l"
print(table)