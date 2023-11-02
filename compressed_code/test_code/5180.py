def solution():
    
    total_students = 100
    grade_4_students = 30
    grade_5_students = 35
    grade_6_students = total_students - grade_4_students - grade_5_students
    result = grade_6_students
    return result

print(solution())