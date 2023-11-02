def solution():
    
    daisies_pots = 30
    roses_pots = daisies_pots * 2
    total_pots = daisies_pots + roses_pots
    initial_pots = 100
    remaining_pots = initial_pots - total_pots
    result = remaining_pots
    return result

print(solution())