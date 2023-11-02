def solution():
    """Tim owns rental properties. He decides to replace all the locks and needs to get 3 keys per lock. He owns two apartment complexes which each have 12 apartments. How many keys does he need to make?"""
    locks_per_apartment = 1
    keys_per_lock = 3
    apartments_per_complex = 12
    complexes = 2
    total_locks = locks_per_apartment * apartments_per_complex * complexes
    total_keys = total_locks * keys_per_lock
    result = total_keys
    return result

print(solution())