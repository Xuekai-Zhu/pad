def solution():
    
    physics_students = 200
    biology_students = physics_students / 2
    girls_ratio = 3
    total_ratio = girls_ratio + 1
    boys_ratio = 1
    boys_in_biology = (boys_ratio / total_ratio) * biology_students
    result = boys_in_biology

    return result

print(solution())