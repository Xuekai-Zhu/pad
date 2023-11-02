def solution():
    
    meatballs_per_plate = 3
    portion_eaten = 2/3
    remaining_meatballs_per_son = meatballs_per_plate - (meatballs_per_plate * portion_eaten)
    total_remaining_meatballs = remaining_meatballs_per_son * 3
    result = total_remaining_meatballs
    return result

print(solution())