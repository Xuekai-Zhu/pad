def solution():
    total_eggs = 900  # The farmer has 900 eggs
    eggs_per_tray = 30  # Each tray holds 30 eggs
    price_per_tray = 2.5  # The farmer sells the farmer for $2.5 per tray

    # Calculate the total number of trays
    total_trays = total_eggs / eggs_per_tray

    # Calculate the total earnings from selling the trays
    total_earnings = total_trays * price_per_tray
    result = total_earnings
    return result

print(solution())