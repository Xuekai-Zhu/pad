def solution():
    eggs_per_day = 3  # Each hen lays 3 eggs a day
    num_hens = 3  # Myrtle has 3 hens
    total_eggs = eggs_per_day * num_hens  # Total eggs per day

    # Total eggs laid in 7 days
    eggs_laid = total_eggs * 7

    # Eggs taken by the neighbor
    eggs_taken = 12

    # Eggs remaining after neighbor took some
    eggs_remaining = eggs_laid - eggs_taken

    # Eggs dropped by Myrtle
    eggs_dropped = 5

    # Eggs Myrtle has left
    eggs_myrtle_has = eggs_remaining - eggs_dropped
    result = eggs_myrtle_has
    return result

print(solution())