def solution():
    
    parakeet_eats_per_day = 2
    parrot_eats_per_day = 14
    finch_eats_per_day = parakeet_eats_per_day / 2
    total_grams_needed = (3 * parakeet_eats_per_day * 7) + (2 * parrot_eats_per_day * 7) + (4 * finch_eats_per_day * 7)
    result = total_grams_needed
    return result

print(solution())