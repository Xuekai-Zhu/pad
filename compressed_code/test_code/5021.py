def solution():
    
    starting_clothes = 100
    donated_to_1st_home = 5
    donated_to_2nd_home = 3 * donated_to_1st_home
    thrown_away = 15
    remaining_clothes = starting_clothes - donated_to_1st_home - donated_to_2nd_home - thrown_away
    result = remaining_clothes
    return result

print(solution())