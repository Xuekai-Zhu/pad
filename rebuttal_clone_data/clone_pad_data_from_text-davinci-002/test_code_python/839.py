def solution():
    children_small = 53
    children_large = 35
    adults = 75
    seniors = 37
    omelets_extra = 25
    eggs_per_small_omelet = 2
    eggs_per_large_omelet = 2
    eggs_per_adult_omelet = 4
    eggs_per_senior_omelet = 3
    total_eggs = (children_small * eggs_per_small_omelet) + (children_large * eggs_per_large_omelet) + (adults * eggs_per_adult_omelet) + (seniors * eggs_per_senior_omelet) + (omelets_extra * eggs_per_large_omelet)
    result = total_eggs
    return result

print(solution())