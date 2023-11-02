def solution():
    """Mrs. Watson is grading 120 final exams from her American History class. On Monday, she grades 60% of the exams. On Tuesday, she grades 75% of the remaining exams. On Wednesday, how many more exams does she need to grade?"""
    total_exams = 120
    monday_grades = total_exams * 0.6
    remaining_exams = total_exams - monday_grades
    tuesday_grades = remaining_exams * 0.75
    exams_left = total_exams - monday_grades - tuesday_grades
    result = exams_left
    return result

print(solution())