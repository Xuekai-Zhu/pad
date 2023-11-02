def solution():
    # Define the hourly rate and number of hours worked per day
    hourly_rate = 20
    hours_per_day = 8

    # Calculate the total daily cost for both bodyguards
    daily_cost = hourly_rate * hours_per_day * 2

    # Calculate the weekly cost for both bodyguards
    weekly_cost = daily_cost * 7

    result = weekly_cost
    return result

print(solution())