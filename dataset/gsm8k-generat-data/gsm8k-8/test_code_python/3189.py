def solution():
    # Calculate the total number of chickens after two years
    starting_chickens = 4
    ending_chickens = starting_chickens * 8

    # Calculate the total number of eggs laid per day
    eggs_per_day = ending_chickens * 6

    # Calculate the total number of eggs collected per week
    eggs_per_week = eggs_per_day * 7
    result = eggs_per_week
    return result

print(solution())