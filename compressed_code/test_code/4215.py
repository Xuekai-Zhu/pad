def solution():
    
    total_students = 100
    boy_ratio = 3
    girl_ratio = 2
    total_ratio_parts = boy_ratio + girl_ratio
    boy_parts = boy_ratio / total_ratio_parts
    girl_parts = girl_ratio / total_ratio_parts
    total_boys = boy_parts * total_students
    total_girls = girl_parts * total_students
    more_boys = total_boys - total_girls
    result = more_boys
    return result

print(solution())