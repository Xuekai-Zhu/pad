def solution():
    eggs_per_tray = 24  # Each tray can hold 24 eggs
    num_trays = 2  # Jaime has 2 trays
    total_eggs = 64  # Jaime has 64 eggs

    # Calculate the total number of trays
    total_trays = num_trays

    # Calculate the total number of eggs used on the trays
    total_eggs_used = total_trays * eggs_per_tray

    # Calculate the number of eggs won't place on the trays
    eggs_left = total_eggs - total_eggs_used
    result = eggs_left
    return result

print(solution())