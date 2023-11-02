def solution():
    """A farmer has 900 eggs. He placed them on a tray, which holds 30 eggs each. How much will the farmer earn if he sells it for $2.5 per tray?"""
    total_eggs = 900
    eggs_per_tray = 30
    trays = total_eggs / eggs_per_tray
    price_per_tray = 2.5
    earnings = trays * price_per_tray
    result = earnings
    return result

print(solution())