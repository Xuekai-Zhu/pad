def solution():
    # Calculate the number of days in one season
    days_per_season = 250 / 5

    # Multiply by the number of seasons the astronaut will spend on Orbius-5
    total_days = days_per_season * 3
    result = total_days
    return result

print(solution())