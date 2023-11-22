def solution():
    
    eggs_per_tray = 24
    total_eggs = 64
    trays = 2
    eggs_on_trays = total_eggs / eggs_per_tray
    eggs_not_on_trays = eggs_on_trays - eggs_per_tray
    result = eggs_not_on_trays
    return result

print(solution())