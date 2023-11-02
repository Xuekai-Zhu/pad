def solution():
    # Number of locks per apartment
    locks_per_apartment = 1  # Assuming only one lock per apartment

    # Total number of locks in both apartment complexes
    total_locks = 2 * 12 * locks_per_apartment

    # Number of keys needed per lock
    keys_per_lock = 3

    # Total number of keys needed
    total_keys = total_locks * keys_per_lock
    result = total_keys
    return result

print(solution())