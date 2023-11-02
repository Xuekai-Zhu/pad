def solution():
    """Tim buys 3 loaves of bread. Each loaf of bread has 20 slices. He pays for the 3 loaves of bread with 2 $20 bills. He gets $16 change. How much does each slice cost, in cents?"""
    # Define the number of loaves of bread and slices per loaf
    loaves = 3
    slices_per_loaf = 20

    # Calculate the total number of slices
    total_slices = loaves * slices_per_loaf

    # Calculate the total cost of the bread
    total_cost = 2 * 20 - 16

    # Calculate the cost per slice, in cents
    cost_per_slice = total_cost / total_slices * 100

    # Return the result
    result = cost_per_slice
    return result

print(solution())