def solution():
    parakeets = 3
    parrots = 2
    finches = 4
    grams_per_parakeet = 2
    grams_per_parrot = 14
    grams_per_finch = grams_per_parakeet / 2
    total_grams = (parakeets * grams_per_parakeet) + (parrots * grams_per_parrot) + (finches * grams_per_finch)
    result = total_grams
    return result

print(solution())