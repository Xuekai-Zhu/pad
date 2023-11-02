def solution():
    trays_collected = 10  # trays of eggs collected initially
    trays_dropped = 2  # trays of eggs dropped accidentally
    trays_added = 7  # trays of eggs added after dropping trays

    # Calculate the total number of trays of eggs sold
    trays_sold = trays_collected - trays_dropped + trays_added

    # Calculate the total number of eggs sold
    eggs_sold = trays_sold * 30  # assuming each tray has 30 eggs

    result = eggs_sold
    return result

print(solution())