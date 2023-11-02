def solution():
    husband_speed = 1
    wife_speed = husband_speed * 2
    husband_time = 3
    wife_time = husband_time / wife_speed
    husband_distance = husband_speed * husband_time
    wife_distance = wife_speed * wife_time
    husband_laps = husband_distance / .25
    wife_laps = wife_distance / .25
    result = wife_laps
    return result

print(solution())