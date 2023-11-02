def solution():
    # Calculate the total cost of the bread
    total_cost = 2*20 + 16  # Tim pays with 2 $20 bills and gets $16 change

    # Calculate the cost of each slice of bread, in cents
    cost_per_slice = total_cost / (3*20) * 100  # 3 loaves, each with 20 slices, multiplied by 100 to get the cost in cents
    result = cost_per_slice
    return result

print(solution())