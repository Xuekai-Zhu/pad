def solution():
    """The number of dishes Sandrine washed was 10 more than the number of bananas Charles cooked.
    Also, the number of bananas Charles cooked was 3 times the number of pears he picked.
    If Charles picked 50 pears, how many dishes did Sandrine wash?"""
    pears_picked = 50
    bananas_cooked = 3 * pears_picked
    dishes_washed = bananas_cooked + 10
    result = dishes_washed
    return result

print(solution())