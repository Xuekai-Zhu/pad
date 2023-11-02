def solution():
    # Calculate the number of hours trained per day
    daily_hours = 2 * 4

    # Calculate the number of days trained per year (excluding 2 rest days per week)
    training_days = 365 - (2 * 52)

    # Calculate the total number of hours trained per year
    total_hours = daily_hours * training_days

    result = total_hours
    return result

print(solution())