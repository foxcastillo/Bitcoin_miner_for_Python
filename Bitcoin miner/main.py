#Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# This was made for EDUCATIONAL PURPOSES ONLY

import hashlib

NONCE_LIMIT = 100000000000

Zeroes = 4

def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * Zeroes):
            print(f"Found Hash with Nonce: {nonce}")
            return hash_try

    return -1
block_number = 24 # Insert here your personal block # 
transactions = "76132fcc2122" # Insert here your transaction #
previous_hash = "876de8756b967c87" 

combined_text = str(block_number) + transactions + previous_hash +str(107617) # Insert here your bitcoin hash #
print(hashlib.sha256(combined_text.encode()).hexdigest())