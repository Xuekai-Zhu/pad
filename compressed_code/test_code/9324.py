def solution():
    
    skirt_cost = 13
    blouse_cost = 6
    num_skirts = 2
    num_blouses = 3
    total_cost = (skirt_cost * num_skirts) + (blouse_cost * num_blouses)
    change = 100 - total_cost
    result = change
    return result

print(solution())