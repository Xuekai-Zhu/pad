def solution():
    # Calculate the total number of eggs being eaten every week
    eggs_per_day = 2 + 2 + 4 + 4  # son and daughter eat 2 eggs each morning, Rhea and husband eat 4 eggs each night
    eggs_per_week = eggs_per_day * 7  # total number of eggs being eaten every week
    trays_per_week = 2  # Rhea buys 2 trays of eggs every week
    eggs_per_tray = 24  # each tray has 24 eggs
    total_eggs_per_week = trays_per_week * eggs_per_tray
    eggs_not_eaten_per_week = total_eggs_per_week - eggs_per_week  # calculate the number of eggs not being eaten every week
    result = eggs_not_eaten_per_week
    return result

print(solution())