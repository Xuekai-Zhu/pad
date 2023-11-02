def solution():
    # Calculate the total number of keys needed by Tim to replace all the locks
    keys_per_lock = 3  # Tim needs 3 keys per lock
    num_apartments = 2 * 12  # Tim owns 2 apartment complexes with 12 apartments each
    num_locks = num_apartments  # Tim needs one lock for each apartment
    total_keys = keys_per_lock * num_locks
    result = total_keys
    return result

print(solution())