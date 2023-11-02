def solution():
    """Monica is wrapping Christmas gifts. She has 6 gifts to wrap for her family, 4 gifts to wrap for her friends, and 2 gifts to wrap for her teachers. She has 144 inches of ribbon and wants to make a bow for each gift with it. How many inches of ribbon can she use for each gift bow?"""
    total_gifts = 6 + 4 + 2
    total_ribbon = 144
    ribbon_per_gift = total_ribbon / total_gifts
    result = ribbon_per_gift
    return result

print(solution())