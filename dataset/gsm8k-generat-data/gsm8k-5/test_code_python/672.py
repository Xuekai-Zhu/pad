def solution():
    carrots_per_day = 1  # Harris feeds his dog 1 carrot per day
    carrots_per_bag = 5  # There are 5 carrots in a 1 pound bag
    cost_per_bag = 2.0  # Each bag of carrots costs $2.00
    days_per_year = 365  # There are 365 days in a year

    # Calculate the total number of bags of carrots needed in a year
    total_carrots = carrots_per_day * days_per_year
    total_bags = total_carrots / carrots_per_bag

    # Calculate the total cost of carrots for the year
    total_cost = total_bags * cost_per_bag
    result = total_cost
    return result

print(solution())