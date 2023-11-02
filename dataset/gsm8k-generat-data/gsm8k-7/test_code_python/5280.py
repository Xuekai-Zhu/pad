def solution():
    initial_trays = 10
    dropped_trays = 2
    added_trays = 7
    eggs_per_tray = 30

    # Calculate the total number of trays after the accident and additional trays
    total_trays = initial_trays - dropped_trays + added_trays

    # Calculate the total number of eggs in all trays
    total_eggs = total_trays * eggs_per_tray

    result = total_eggs
    return result

print(solution())