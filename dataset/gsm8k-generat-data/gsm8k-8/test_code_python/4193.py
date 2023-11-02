def solution():
    # Calculate the total minutes Hayden spends ironing each day
    daily_minutes = 5 + 3 

    # Calculate the total minutes Hayden spends ironing each week
    weekly_minutes = daily_minutes * 5 

    # Calculate the total minutes Hayden spends ironing over 4 weeks
    monthly_minutes = weekly_minutes * 4

    result = monthly_minutes
    return result

print(solution())