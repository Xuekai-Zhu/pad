def solution():
    """Noah has two closets. Each closet can fit 1/4 as much as Ali's closet, which can fit 200 pairs of jeans. How many jeans can both Noah’s closets fit?"""
    ali_closet_capacity = 200
    noah_closet_capacity = ali_closet_capacity / 4
    total_noah_capacity = 2 * noah_closet_capacity
    jeans_per_closet = total_noah_capacity
    result = jeans_per_closet
    return result

print(solution())