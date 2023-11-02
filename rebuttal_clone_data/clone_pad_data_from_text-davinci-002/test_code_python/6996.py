def solution():
    raise_per_hour = 0.50
    hours_worked_per_week = 40
    reduced_housing_benefit = 60
    weekly_earnings = (raise_per_hour * hours_worked_per_week) - reduced_housing_benefit
    result = weekly_earnings
    return result

print(solution())