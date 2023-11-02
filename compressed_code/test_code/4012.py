def solution():
    
    total_students = 325
    glasses_percent = 40
    students_with_glasses = (glasses_percent / 100) * total_students
    students_without_glasses = total_students - students_with_glasses
    result = students_without_glasses
    return result

print(solution())