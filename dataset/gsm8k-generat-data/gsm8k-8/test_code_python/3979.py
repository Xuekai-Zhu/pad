def solution():
    weekly_cost = 36
    cost_per_gallon = 3

    # Calculate the number of gallons used in one week
    gallons_per_week = weekly_cost / cost_per_gallon

    # Double the number of gallons used to find the total for two weeks
    total_gallons = gallons_per_week * 2
    result = total_gallons
    return result

print(solution())