def solution():
    total_students = 325
    glasses_percentage = 40
    glasses_students = (glasses_percentage / 100) * total_students
    no_glasses_students = total_students - glasses_students
    result = no_glasses_students
    return result

print(solution())