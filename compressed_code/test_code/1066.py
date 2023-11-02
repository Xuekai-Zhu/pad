def solution():
    
    total_pots = 60
    pots_per_set = 5
    sets_per_shelf = 3
    pots_per_shelf = pots_per_set * sets_per_shelf
    total_shelves = total_pots / pots_per_shelf
    result = total_shelves
    return result

print(solution())