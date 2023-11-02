def solution():
    """Karen and Donald and their 6 children are sharing a beach house with Tom and Eva and their 4 children. 
    If there are 16 legs in the pool, how many people are not in the pool?"""
    karen_and_donald = 2 + 6
    tom_and_eva = 2 + 4
    total_people = karen_and_donald + tom_and_eva
    legs_in_pool = 16
    legs_outside_pool = total_people * 2 - legs_in_pool
    people_not_in_pool = legs_outside_pool / 2
    result = people_not_in_pool
    return result

print(solution())