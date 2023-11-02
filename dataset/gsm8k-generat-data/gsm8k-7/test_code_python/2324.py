def solution():
    hourly_rate = 5
    num_hours_per_day = 5
    num_afternoons_per_week = 6
    num_weeks = 7

    # Calculate the total number of hours Isabella babysits in one week
    total_hours_per_week = num_hours_per_day * num_afternoons_per_week

    # Calculate the total amount of money Isabella earns in one week
    weekly_earnings = total_hours_per_week * hourly_rate

    # Calculate the total amount of money Isabella earns in seven weeks
    total_earnings = weekly_earnings * num_weeks
    result = total_earnings
    return result

print(solution())