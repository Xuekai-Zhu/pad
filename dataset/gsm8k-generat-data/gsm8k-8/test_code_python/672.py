def solution():
    carrots_per_day = 1
    carrots_per_bag = 5
    cost_per_bag = 2.00

    # Calculate the number of bags needed per day
    bags_per_day = carrots_per_day / carrots_per_bag

    # Calculate the cost per day
    cost_per_day = bags_per_day * cost_per_bag

    # Calculate the cost per year (365 days)
    cost_per_year = cost_per_day * 365

    result = cost_per_year
    return result

print(solution())