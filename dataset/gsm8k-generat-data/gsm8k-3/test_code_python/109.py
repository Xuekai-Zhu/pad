def solution():
    """Alyssa, Keely, and Kendall ordered 100 chicken nuggets from a fast-food restaurant. Keely and Kendall each ate twice as many as Alyssa. How many did Alyssa eat?"""
    # Define the total number of chicken nuggets ordered
    total_nuggets = 100

    # Calculate the number of nuggets Keely and Kendall ate combined
    keely_kendall_nuggets = total_nuggets - (total_nuggets / 4)

    # Calculate the number of nuggets Alyssa ate
    alyssa_nuggets = (total_nuggets - keely_kendall_nuggets) / 2

    # Return the result
    result = alyssa_nuggets
    return result

print(solution())