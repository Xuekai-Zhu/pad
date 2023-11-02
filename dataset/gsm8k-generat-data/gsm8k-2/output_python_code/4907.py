def solution():
    """Noah has two closets. Each closet can fit 1/4 as much as Ali's closet, which can fit 200 pairs of jeans. How many jeans can both Noah’s closets fit?"""
    ali_closet_capacity = 200
    noah_closet_capacity = ali_closet_capacity / 4
    total_noah_capacity = noah_closet_capacity * 2
    result = total_noah_capacity
    return result

print(solution())