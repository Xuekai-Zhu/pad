def solution():
    """Rhea buys 2 trays of eggs every week for her family. Her son and daughter eat 2 eggs every morning, and Rhea and her husband eat 4 eggs every night. If each tray has 24 eggs, how many eggs are not being eaten every week?"""
    trays_per_week = 2
    eggs_per_tray = 24
    eggs_per_day = 2 + 2 + 4 + 4  # total eggs eaten per day
    eggs_not_eaten = trays_per_week * eggs_per_tray - eggs_per_day * 7
    result = eggs_not_eaten
    return result

print(solution())