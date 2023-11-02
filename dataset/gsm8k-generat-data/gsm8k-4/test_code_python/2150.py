def solution():
    """Rhea buys 2 trays of eggs every week for her family. Her son and daughter eat 2 eggs every morning, and Rhea and her husband eat 4 eggs every night. If each tray has 24 eggs, how many eggs are not being eaten every week?"""
    # Define the number of eggs per tray
    EGGS_PER_TRAY = 24

    # Define the number of eggs eaten by Rhea's son and daughter every week
    eggs_per_day_kids = 2 * 7
    eggs_per_week_kids = eggs_per_day_kids * 2

    # Define the number of eggs eaten by Rhea and her husband every week
    eggs_per_day_adults = 4 * 7
    eggs_per_week_adults = eggs_per_day_adults * 2

    # Calculate the total number of eggs eaten every week
    total_eggs_eaten = eggs_per_week_kids + eggs_per_week_adults

    # Calculate the number of eggs remaining every week
    eggs_remaining = (2 * EGGS_PER_TRAY) - total_eggs_eaten

    result = eggs_remaining
    return result

print(solution())