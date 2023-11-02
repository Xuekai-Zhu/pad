def solution():
    weekly_cost = 36  # dollars spent per week on diesel fuel
    cost_per_gallon = 3  # cost of diesel fuel per gallon
    gallons_per_week = weekly_cost / cost_per_gallon  # gallons of diesel fuel used per week
    gallons_per_two_weeks = gallons_per_week * 2  # gallons of diesel fuel used in two weeks
    result = gallons_per_two_weeks
    return result

print(solution())