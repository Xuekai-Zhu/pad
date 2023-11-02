def solution():
    
    initial_cats = 20
    new_cats = 2
    injured_cats = 1
    adopted_cats = 3 * 2
    total_cats = initial_cats + new_cats + injured_cats - adopted_cats
    result = total_cats
    return result

print(solution())