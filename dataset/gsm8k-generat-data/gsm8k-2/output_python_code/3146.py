def solution():
    """Peter needs to buy birdseed to last a week. He knows that each parakeet eats 2 grams a day. His parrots eat 14 grams a day.
    His finches eat half of what a parakeet eats. If he has 3 parakeets, 2 parrots and 4 finches, how many grams of birdseed does he need to buy?"""
    parakeet_eats_per_day = 2
    parrot_eats_per_day = 14
    finch_eats_per_day = parakeet_eats_per_day / 2
    total_grams_needed = (3 * parakeet_eats_per_day * 7) + (2 * parrot_eats_per_day * 7) + (4 * finch_eats_per_day * 7)
    result = total_grams_needed
    return result

print(solution())