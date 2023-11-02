def solution():
    # Define the cost of each item
    shower_gel_cost = 4
    toothpaste_cost = 3

    # Calculate the total spent on shower gels
    total_shower_gel_cost = shower_gel_cost * 4

    # Calculate the remaining budget after buying shower gels and toothpaste
    remaining_budget = 60 - total_shower_gel_cost - toothpaste_cost - 30

    # The remaining budget equals the cost of the laundry detergent
    laundry_detergent_cost = remaining_budget

    result = laundry_detergent_cost
    return result

print(solution())