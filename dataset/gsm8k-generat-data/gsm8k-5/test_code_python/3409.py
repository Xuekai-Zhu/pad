def solution():
    ounces_per_can = 8  # Each can contains 8 ounces of soda
    total_ounces = 80  # Peter needs 80 ounces of soda for his party
    cans_needed = total_ounces / ounces_per_can  # Calculate the number of cans needed

    # Calculate the total cost of the cans of soda
    cost_per_can = 0.5
    total_cost = cans_needed * cost_per_can
    result = total_cost
    return result

print(solution())