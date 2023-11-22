def solution():
    
    total_students = 200
    boys = (2/5) * total_students
    girls = (2/3) * total_students
    non_girls = total_students - boys - girls
    result = non_girls
    return result

print(solution())