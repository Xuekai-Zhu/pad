def solution():
    """Tim owns rental properties.  He decides to replace all the locks and needs to get 3 keys per lock.  He owns two apartment complexes which each have 12 apartments.  How many keys does he need to make?"""
    # Define the number of apartments per complex and the number of complexes
    apartments_per_complex = 12
    num_complexes = 2

    # Calculate the total number of apartments
    total_apartments = apartments_per_complex * num_complexes

    # Calculate the total number of locks and keys needed
    num_locks = total_apartments
    num_keys = num_locks * 3

    # Display the total number of keys needed
    result = num_keys
    return result

print(solution())