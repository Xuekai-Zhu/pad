def solution():
    # Rainfall on the first day
    day1_rainfall = 4

    # Rainfall on the second day (5 times as much as the first day)
    day2_rainfall = 5 * day1_rainfall

    # Rainfall on the third day (6 inches less than the sum of the first two days)
    day3_rainfall = day1_rainfall + day2_rainfall - 6

    result = day3_rainfall
    return result

print(solution())