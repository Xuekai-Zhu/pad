def solution():
    """Austin has 10 pairs of dress shoes he needs to polish over the weekend. If he has polished 45% of individual shoes, how many more shoes does he need to polish?"""
    total_pairs = 10
    shoes_per_pair = 2
    polished_percent = 45
    polished_shoes = total_pairs * shoes_per_pair * (polished_percent / 100)
    remaining_shoes = total_pairs * shoes_per_pair - polished_shoes
    result = remaining_shoes
    return result

print(solution())