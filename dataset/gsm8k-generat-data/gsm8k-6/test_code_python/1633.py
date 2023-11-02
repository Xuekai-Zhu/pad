def solution():
    # Calculate the total number of chocolates eaten on weekdays and weekends
    weekdays_chocolates = 2 * 5  # Erwin eats 2 chocolates on weekdays
    weekends_chocolates = 1 * 2  # Erwin eats 1 chocolate on weekends
    total_chocolates = weekdays_chocolates + weekends_chocolates

    # Calculate the number of weeks it took to finish all the chocolates
    weeks = total_chocolates / 24

    result = weeks
    return result

print(solution())