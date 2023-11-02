def solution():
    """Alyssa, Keely, and Kendall ordered 100 chicken nuggets from a fast-food restaurant. Keely and Kendall each ate twice as many as Alyssa. How many did Alyssa eat?"""
    # Define the total number of chicken nuggets
    total_nuggets = 100

    # Define the ratio of nuggets eaten by Alyssa, Keely, and Kendall
    alyssa_ratio = 1
    keely_ratio = 2
    kendall_ratio = 2

    # Calculate the total ratio of nuggets eaten
    total_ratio = alyssa_ratio + keely_ratio + kendall_ratio

    # Calculate the number of nuggets eaten by Alyssa
    alyssa_nuggets = (alyssa_ratio / total_ratio) * total_nuggets

    # Round the result to the nearest whole number
    result = round(alyssa_nuggets)
    return result

print(solution())