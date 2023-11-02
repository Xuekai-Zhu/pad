def solution():
    trays_bought = 2
    eggs_per_tray = 24
    eggs_eaten_daily = 2 + 2 + 4 + 4
    eggs_not_eaten = trays_bought * eggs_per_tray - eggs_eaten_daily
    result = eggs_not_eaten
    return result

print(solution())