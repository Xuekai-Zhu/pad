def solution():
    trays_per_week = 2  # Rhea buys 2 trays of eggs every week
    eggs_per_tray = 24  # Each tray has 24 eggs
    total_eggs = trays_per_week * eggs_per_tray  # Total number of eggs Rhea buys every week

    # Calculate the number of eggs consumed by Rhea's family every week
    eggs_consumed = (2 * 7 * 2) + (4 * 7 * 2)  # Rhea's son and daughter eat 2 eggs every morning, while Rhea and her husband eat 4 eggs every night for 7 days a week

    # Calculate the number of eggs not being eaten every week
    eggs_not_eaten = total_eggs - eggs_consumed
    result = eggs_not_eaten
    return result

print(solution())