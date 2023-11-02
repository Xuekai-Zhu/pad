def solution():
    # Calculate the total number of visitors for the first 6 days
    daily_visitors = 100
    total_visitors_first_six_days = daily_visitors * 6

    # Calculate the total number of visitors on the last day
    total_visitors_other_days = daily_visitors * 6
    last_day_visitors = 2 * total_visitors_other_days

    # Calculate the total number of visitors for the week
    total_visitors = total_visitors_first_six_days + last_day_visitors

    # Calculate Tim's earnings for the week
    earnings = total_visitors * 0.01
    result = earnings
    return result

print(solution())