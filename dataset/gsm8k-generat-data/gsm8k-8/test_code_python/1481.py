def solution():
    # Calculate the total hours Mike spends watching TV each week
    tv_hours_per_day = 4
    tv_hours_per_week = tv_hours_per_day * 7

    # Calculate the total hours Mike spends playing video games each week
    games_days_per_week = 3
    games_hours_per_day = tv_hours_per_day / 2
    games_hours_per_week = games_days_per_week * games_hours_per_day

    # Calculate the total hours Mike spends watching TV and playing video games each week
    total_hours_per_week = tv_hours_per_week + games_hours_per_week
    result = total_hours_per_week
    return result

print(solution())