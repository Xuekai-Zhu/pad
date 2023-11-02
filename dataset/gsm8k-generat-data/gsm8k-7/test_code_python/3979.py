def solution():
    weekly_cost = 36
    cost_per_gallon = 3
    num_weeks = 2

    # Calculate the total cost of diesel fuel for two weeks
    total_cost = weekly_cost * num_weeks

    # Calculate the total number of gallons of diesel fuel used in two weeks
    total_gallons = total_cost / cost_per_gallon
    result = total_gallons
    return result

print(solution())