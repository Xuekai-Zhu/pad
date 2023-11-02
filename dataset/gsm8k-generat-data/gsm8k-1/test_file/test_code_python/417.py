def solution():
    """There were 50 cats on a rock. Four boats came and carried away 5 cats each, and later, 3/5 of the remaining cats ran after a mouse they'd seen. How many cats were left on the rock?"""
    initial_cats = 50
    cats_carried_away = 4 * 5
    remaining_cats = initial_cats - cats_carried_away
    cats_chasing_mouse = remaining_cats * (3/5)
    cats_left = remaining_cats - cats_chasing_mouse
    result = cats_left
    
    return result

print(solution())