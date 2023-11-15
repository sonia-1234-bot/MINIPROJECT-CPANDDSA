# Example 1: Hashing integers
number = 42
hash_value = hash(number)
print(f"Hash value of {number}: {hash_value}")

# Example 2: Hashing strings
string_data = "Hello, Hashing!"
hash_value_string = hash(string_data)
print(f"Hash value of '{string_data}': {hash_value_string}")


import hashlib

# Example: Cryptographic hashing using hashlib
data = b"Hello, Cryptographic Hashing!"
hash_object = hashlib.sha256(data)
print(hash_object)
hash_value_crypto = hash_object.hexdigest()
print(f"Cryptographic hash value: {hash_value_crypto}")
