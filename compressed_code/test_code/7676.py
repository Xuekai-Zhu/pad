def solution():
    
    initial_cats = 6
    new_cats = 12
    adopted_cats = 3
    kitten_cats = 5
    missing_cats = 1
    total_cats = initial_cats + new_cats - adopted_cats + kitten_cats - missing_cats
    result = total_cats
    return result

print(solution())