def solution():
    num_sheets_per_ream = 500
    cost_per_ream = 27
    num_sheets_needed = 5000

    # Calculate the total number of reams needed
    num_reams_needed = num_sheets_needed / num_sheets_per_ream

    # Round up to the nearest whole number of reams
    num_reams_needed = math.ceil(num_reams_needed)

    # Calculate the total cost of all reams needed
    total_cost = num_reams_needed * cost_per_ream
    result = total_cost
    return result

print(solution())