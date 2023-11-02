def solution():
    hours_per_week = 35
    hourly_rate = 10
    num_days = 5
    total_hours = hours_per_week * 2

    # Calculate the total amount Arman earned last week
    total_last_week_earnings = hours_per_week * hourly_rate * num_days

    # Calculate the new hourly rate for this week
    new_hourly_rate = hourly_rate + 0.5

    # Calculate the total earnings for this week
    total_this_week_earnings = new_hourly_rate * (total_hours - hours_per_week)

    # Calculate the total earnings for two weeks
    total_earnings = total_last_week_earnings + total_this_week_earnings
    result = total_earnings
    return result

print(solution())