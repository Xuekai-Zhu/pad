def solution():
    """There are 3 meatballs on each spaghetti plate. If Theresa's 3 sons each eat two-thirds of the meatballs on their respective plates, how many meatballs are still left on their plates altogether?"""
    meatballs_per_plate = 3
    sons = 3
    eaten_fraction = 2/3
    total_meatballs_eaten = sons * meatballs_per_plate * eaten_fraction
    total_meatballs_left = (meatballs_per_plate * sons) - total_meatballs_eaten
    result = total_meatballs_left
    return result

print(solution())