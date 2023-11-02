def solution():
    """Karen and Donald and their 6 children are sharing a beach house with Tom and Eva and their 4 children. If there are 16 legs in the pool, how many people are not in the pool?"""
    karen_donald_legs = 2 * 2
    karen_donald_children_legs = 6 * 2
    tom_eva_legs = 2 * 2
    tom_eva_children_legs = 4 * 2
    total_legs_in_pool = 16
    total_legs_not_in_pool = karen_donald_legs + karen_donald_children_legs + tom_eva_legs + tom_eva_children_legs - total_legs_in_pool
    total_people_not_in_pool = (karen_donald_children_legs / 2) + (tom_eva_children_legs / 2) + 2
    result = total_people_not_in_pool
    return result

print(solution())