def solution():
    """Alyssa, Keely, and Kendall ordered 100 chicken nuggets from a fast-food restaurant. Keely and Kendall each ate twice as many as Alyssa. How many did Alyssa eat?"""
    total_nuggets = 100
    keely_nuggets = 2 * alyssa_nuggets
    kendall_nuggets = 2 * alyssa_nuggets
    alyssa_nuggets = (total_nuggets - keely_nuggets - kendall_nuggets) / 5
    result = alyssa_nuggets
    return result

print(solution())