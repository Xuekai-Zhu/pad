def solution():
    # Define the total number of nuggets
    total_nuggets = 100

    # Calculate how many nuggets Keely and Kendall each ate
    keely_nuggets = 2 * alyssa_nuggets
    kendall_nuggets = 2 * alyssa_nuggets

    # Calculate how many nuggets Alyssa ate
    alyssa_nuggets = (total_nuggets - keely_nuggets - kendall_nuggets) / 4

    result = alyssa_nuggets
    return result

print(solution())