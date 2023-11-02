def solution():
    """There are 3 meatballs on each spaghetti plate. If Theresa's 3 sons each eat two-thirds of the meatballs on their respective plates, how many meatballs are still left on their plates altogether?"""
    meatballs_per_plate = 3
    portion_eaten = 2/3
    remaining_meatballs_per_son = meatballs_per_plate - (meatballs_per_plate * portion_eaten)
    total_remaining_meatballs = remaining_meatballs_per_son * 3
    result = total_remaining_meatballs
    return result

print(solution())