def solution():
    
    initial_cats = 28
    initial_dogs = 18
    adopted_cats = 3
    remaining_cats = initial_cats - adopted_cats
    remaining_dogs = initial_dogs
    cat_diff = remaining_cats - remaining_dogs
    result = cat_diff
    return result

print(solution())