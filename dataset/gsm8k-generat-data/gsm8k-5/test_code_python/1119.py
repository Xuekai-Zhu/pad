def solution():
    first_day_minutes = 5  # Jill spends 5 minutes talking on the first day
    total_minutes = first_day_minutes  # Add the minutes from the first day to the total

    # Calculate the minutes Jill spends on the phone each subsequent day and add to the total
    for day in range(2, 6):
        minutes = first_day_minutes * (2 ** (day - 2))
        total_minutes += minutes

    result = total_minutes
    return result

print(solution())