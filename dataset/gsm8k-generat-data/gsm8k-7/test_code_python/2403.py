def solution():
    onur_daily_distance = 250
    hanil_daily_distance = onur_daily_distance + 40
    num_days_per_week = 5

    # Calculate the total distance Onur bikes in a week
    onur_weekly_distance = onur_daily_distance * num_days_per_week

    # Calculate the total distance Hanil bikes in a week
    hanil_weekly_distance = hanil_daily_distance * num_days_per_week

    # Calculate the total distance the two friends bikes in a week
    total_weekly_distance = onur_weekly_distance + hanil_weekly_distance
    result = total_weekly_distance
    return result

print(solution())