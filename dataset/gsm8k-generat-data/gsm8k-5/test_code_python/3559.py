def solution():
    # Calculate the total cost of the 3 loaves of bread
    cost = 2 * 20 + 16  # Tim pays with 2 $20 bills and gets $16 change
    total_slices = 3 * 20  # There are 20 slices in each loaf

    # Calculate the cost per slice in cents
    cost_per_slice = (cost * 100) / total_slices
    result = cost_per_slice
    return result

print(solution())