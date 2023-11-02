def solution():
    """It takes 7 years for an apple tree to bear fruit. If Lydia planted a tree when she was 4 years old and is now 9 years old, how old would she be when she gets to eat an apple from her tree for the first time?"""
    tree_age = 9 - 4
    fruit_age = 7
    years_to_fruit = fruit_age - tree_age
    lydia_fruit_age = 9 + years_to_fruit
    result = lydia_fruit_age
    return result

print(solution())