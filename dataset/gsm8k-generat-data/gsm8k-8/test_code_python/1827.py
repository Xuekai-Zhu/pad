def solution():
    # Calculate the number of eggs Lisa makes each day
    eggs_per_day = 2 * 4 + 3 + 2

    # Calculate the number of eggs Lisa makes in a week
    eggs_per_week = eggs_per_day * 5

    # Calculate the number of eggs Lisa makes in a year
    eggs_per_year = eggs_per_week * 52

    result = eggs_per_year
    return result

print(solution())