def solution():
    
    total_cats = 1800
    first_mission_cats = 600
    remaining_cats = total_cats - first_mission_cats
    second_mission_cats = remaining_cats // 2
    remaining_cats = remaining_cats - second_mission_cats
    result = remaining_cats
    return result

print(solution())