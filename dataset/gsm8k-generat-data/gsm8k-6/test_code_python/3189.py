def solution():
    # Calculate the number of chickens Gary has after 2 years
    chickens_after_2_years = 4 * 8

    # Calculate the number of eggs collected by Gary per day
    eggs_per_day = chickens_after_2_years * 6

    # Calculate the number of eggs collected by Gary per week
    eggs_per_week = eggs_per_day * 7

    result = eggs_per_week
    return result

print(solution())