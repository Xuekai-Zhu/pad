def solution():
    cats_on_island = 1800
    cats_relocated_first_mission = 600
    cats_relocated_second_mission = (cats_on_island - cats_relocated_first_mission) / 2
    cats_remaining = cats_on_island - cats_relocated_first_mission - cats_relocated_second_mission
    result = cats_remaining
    
    return result

print(solution())