def solution():
    
    initial_cats = 1800
    first_mission_cats = 600
    remaining_cats = initial_cats - first_mission_cats
    second_mission_cats = remaining_cats / 2
    cats_on_island_after_missions = remaining_cats - second_mission_cats
    result = cats_on_island_after_missions
    return result

print(solution())