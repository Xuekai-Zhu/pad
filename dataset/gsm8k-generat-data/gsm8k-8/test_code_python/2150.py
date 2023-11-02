def solution():
    # Define the number of trays and eggs eaten per day
    trays_per_week = 2
    eggs_per_day = 2 + 2 + 4 + 4

    # Calculate the number of eggs eaten per week
    eggs_per_week = trays_per_week * 24 * 7 * eggs_per_day

    # Calculate the number of eggs not eaten per week
    eggs_not_eaten = (7 * 12) - eggs_per_week
    result = eggs_not_eaten
    return result

print(solution())