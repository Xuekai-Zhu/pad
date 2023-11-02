def solution():
    """Peter needs to buy birdseed to last a week. He knows that each parakeet eats 2 grams a day. His parrots eat 14 grams a day. His finches eat half of what a parakeet eats. If he has 3 parakeets, 2 parrots and 4 finches, how many grams of birdseed does he need to buy?"""
    parakeets = 3
    parrot_weight = 14
    parrot_count = 2
    finch_weight = 1 # 1/2 of a parakeet's weight
    finch_count = 4
    total_weight = (parakeets * 2 + parrot_weight * parrot_count + finch_weight * finch_count) * 7 # 7 days in a week
    result = total_weight
    return result

print(solution())