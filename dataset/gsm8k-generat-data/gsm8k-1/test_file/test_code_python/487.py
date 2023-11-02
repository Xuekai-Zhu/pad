def solution():
    """Jaime places eggs on the tray. Each tray can hold 24 eggs. If he has 64 eggs and 2 trays, how many eggs won't he be able to place on the tray?"""
    eggs = 64
    trays = 2
    eggs_on_trays = trays * 24
    eggs_left = eggs - eggs_on_trays
    result = eggs_left
    return result

print(solution())