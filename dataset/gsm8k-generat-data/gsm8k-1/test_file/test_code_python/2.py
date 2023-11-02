def solution():
    """Toulouse has twice as many sheep as Charleston. Charleston has 4 times as many sheep as Seattle. How many sheep do Toulouse, Charleston, and Seattle have together if Seattle has 20 sheep?"""
    seattle_sheep = 20
    charleston_sheep = seattle_sheep * 4
    toulouse_sheep = charleston_sheep * 2
    total_sheep = seattle_sheep + charleston_sheep + toulouse_sheep
    result = total_sheep
    return result

print(solution())