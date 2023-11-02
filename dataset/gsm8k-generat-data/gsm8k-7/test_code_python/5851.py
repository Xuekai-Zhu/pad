def solution():
    crickets_per_week_at_90 = 4
    crickets_per_week_at_100 = 8

    total_weeks = 15
    total_crickets = 0

    for i in range(total_weeks):
        if i < total_weeks * 0.8:  # 90% of the time
            total_crickets += crickets_per_week_at_90
        else:  # 10% of the time
            total_crickets += crickets_per_week_at_100

    result = total_crickets
    return result

print(solution())