def solution():
    
    total_exams = 120
    monday_grades = total_exams * 0.6
    remaining_exams = total_exams - monday_grades
    tuesday_grades = remaining_exams * 0.75
    exams_left = total_exams - monday_grades - tuesday_grades
    result = exams_left
    return result

print(solution())