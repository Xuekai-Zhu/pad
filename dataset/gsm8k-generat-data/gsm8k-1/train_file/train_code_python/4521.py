def solution():
    """Tim owns rental properties. He decides to replace all the locks and needs to get 3 keys per lock. He owns two apartment complexes which each have 12 apartments. How many keys does he need to make?"""
    number_of_apartment_complexes = 2
    apartments_per_complex = 12
    locks_per_apartment = 2
    keys_per_lock = 3
    total_locks = number_of_apartment_complexes * apartments_per_complex * locks_per_apartment
    total_keys = total_locks * keys_per_lock
    result = total_keys
    return result

print(solution())