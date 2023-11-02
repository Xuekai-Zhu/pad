def solution():
    trays_collected = 10  # Haman was asked to collect 10 trays
    trays_dropped = 2  # Haman accidentally dropped two trays
    trays_added = 7  # Haman's father asked him to add 7 more trays

    # Calculate the total number of trays collected after dropping and adding some
    total_trays = trays_collected - trays_dropped + trays_added

    # Calculate how many eggs were sold that day, assuming 30 eggs per tray
    eggs_sold = total_trays * 30
    result = eggs_sold
    return result

print(solution())