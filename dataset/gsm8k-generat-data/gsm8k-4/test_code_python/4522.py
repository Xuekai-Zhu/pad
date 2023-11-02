def solution():
    """Tim owns rental properties. He decides to replace all the locks and needs to get 3 keys per lock. He owns two apartment complexes which each have 12 apartments. How many keys does he need to make?"""
    # Define the number of locks per apartment
    locks_per_apartment = 1

    # Define the number of apartments per complex
    apartments_per_complex = 12

    # Define the number of complexes
    number_of_complexes = 2

    # Calculate the total number of locks
    total_locks = locks_per_apartment * apartments_per_complex * number_of_complexes

    # Calculate the total number of keys needed
    total_keys = total_locks * 3

    # return the result
    result = total_keys
    return result

print(solution())