def solution():
    """Rhea buys 2 trays of eggs every week for her family. Her son and daughter eat 2 eggs every morning, and Rhea and her husband eat 4 eggs every night. If each tray has 24 eggs, how many eggs are not being eaten every week?"""
    trays_per_week = 2
    eggs_per_tray = 24
    morning_eaters = 2 + 2 # son and daughter
    night_eaters = 4 + 4 # Rhea and husband
    eggs_per_day = morning_eaters + night_eaters
    eggs_per_week = eggs_per_day * 7
    eggs_consumed_per_week = eggs_per_week * trays_per_week
    eggs_not_consumed_per_week = (trays_per_week * eggs_per_tray) - eggs_consumed_per_week
    result = eggs_not_consumed_per_week
    return result

print(solution())