def solution():
    # Define the number of locks and keys needed per lock
    locks = 24 # Two apartment complexes with 12 apartments each
    keys_per_lock = 3

    # Calculate the total number of keys needed
    total_keys = locks * keys_per_lock
    result = total_keys
    return result

print(solution())