def solution():
    locks_per_apartment = 1
    keys_per_lock = 3
    apartments_per_complex = 12
    complexes = 2
    total_locks = locks_per_apartment * apartments_per_complex * complexes
    total_keys = keys_per_lock * total_locks
    result = total_keys
    return result

print(solution())