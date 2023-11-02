def solution():
    # Let x be the number of large animals
    # Then, the number of small animals = 3x
    # We know that 4x + 2(3x) = 12
    # Simplifying, we get 10x = 12
    # So, x = 1.2 (which we can round up to 2, since we can't have a fraction of an animal)

    num_large_animals = 2
    num_small_animals = 6

    # Calculate the total sticks of wax used for large animals
    wax_for_large_animals = num_large_animals * 4

    # Calculate the total sticks of wax used for small animals
    wax_for_small_animals = num_small_animals * 2

    # Calculate the total sticks of wax used for all animals
    total_wax_used = wax_for_large_animals + wax_for_small_animals
    result = total_wax_used
    return result

print(solution())