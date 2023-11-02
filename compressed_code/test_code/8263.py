def solution():
    
    vans = 6
    minibusses = 4
    students_per_van = 10
    students_per_minibus = 24
    total_students = (vans * students_per_van) + (minibusses * students_per_minibus)
    result = total_students
    return result

print(solution())