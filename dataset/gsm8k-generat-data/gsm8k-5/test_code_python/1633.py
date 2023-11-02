def solution():
    chocolates_per_weekday = 2  # Erwin eats 2 chocolates on weekdays
    chocolates_per_weekend = 1  # Erwin eats 1 chocolate on weekends
    total_chocolates = 24  # Erwin ate a total of 24 chocolates

    # Calculate the total number of weekday chocolates Erwin ate
    weekday_chocolates = chocolates_per_weekday * 5  # There are 5 weekdays in a week

    # Calculate the total number of weekend chocolates Erwin ate
    weekend_chocolates = chocolates_per_weekend * 2  # There are 2 weekends in a week

    # Calculate the total number of weeks it took Erwin to finish all the chocolates
    total_weeks = (total_chocolates - weekday_chocolates - weekend_chocolates) / chocolates_per_weekend
    result = total_weeks
    return result

print(solution())