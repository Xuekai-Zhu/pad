def solution():
    """Alyssa, Keely, and Kendall ordered 100 chicken nuggets from a fast-food restaurant.
    Keely and Kendall each ate twice as many as Alyssa. How many did Alyssa eat?"""
    total_nuggets = 100
    alyssa_ratio = 1
    keely_ratio = 2
    kendall_ratio = 2
    total_ratio = alyssa_ratio + keely_ratio + kendall_ratio
    alyssa_nuggets = (alyssa_ratio / total_ratio) * total_nuggets
    result = alyssa_nuggets
    return result

print(solution())