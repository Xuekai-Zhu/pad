def solution():
    carrots_per_day = 1
    carrots_per_bag = 5
    cost_per_bag = 2.0
    days_per_year = 365

    # Calculate the total number of carrots Harris will need in a year
    total_carrots = carrots_per_day * days_per_year

    # Calculate the total number of bags of carrots Harris will need in a year
    total_bags = total_carrots / carrots_per_bag

    # Calculate the total cost of all bags of carrots Harris will need in a year
    total_cost = total_bags * cost_per_bag
    result = total_cost
    return result

print(solution())