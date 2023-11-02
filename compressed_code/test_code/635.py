def solution():
    
    small_children = 53
    older_children = 35
    adults = 75
    seniors = 37

    eggs_per_half_omelet = 1
    eggs_per_whole_omelet = 2
    eggs_per_one_and_half_omelets = 3

    total_omelets = (small_children * 0.5) + (older_children * 1) + (adults * 2) + (seniors * 1.5) + 25

    total_eggs = 2 * (total_omelets)

    result = total_eggs
    return result

print(solution())