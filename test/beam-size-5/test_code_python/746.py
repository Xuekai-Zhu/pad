def solution():
    # Calculate the total number of chairs rented during weekdays
    weekday_rented = 60 * 5

    # Calculate the total number of chairs rented during weekends
    weekend_rented = 100 * 2

    # Calculate the total number of chairs rented in two 4-week months
    total_rented = weekday_rented + weekend_rented
    result = total_rented
    return result

print(solution())