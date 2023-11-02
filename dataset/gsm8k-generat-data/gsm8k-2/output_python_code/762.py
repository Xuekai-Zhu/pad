def solution():
    """Josh has 18 yards of ribbon that is to be used equally to 6 gifts. If each gift will use 2 yards of ribbon, how many yards of ribbon will be left?"""
    ribbon_per_gift = 2
    total_gifts = 6
    total_ribbon = ribbon_per_gift * total_gifts
    remaining_ribbon = 18 - total_ribbon
    result = remaining_ribbon
    return result

print(solution())