def solution():
    trays_per_week = 2
    eggs_per_tray = 24
    total_eggs_per_week = trays_per_week * eggs_per_tray

    # Calculate the number of eggs needed per day by the family
    eggs_needed_per_day = (2 + 2) * 2 + (4 + 4)

    # Calculate the total number of eggs needed per week
    total_eggs_needed = eggs_needed_per_day * 7

    # Calculate the number of eggs not being eaten
    eggs_not_eaten = total_eggs_per_week - total_eggs_needed
    result = eggs_not_eaten
    return result

print(solution())