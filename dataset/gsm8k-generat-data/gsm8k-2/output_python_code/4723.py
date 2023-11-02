def solution():
    """Mrs. Watson is grading 120 final exams from her American History class. On Monday, she grades 60% of the exams. On Tuesday, she grades 75% of the remaining exams. On Wednesday, how many more exams does she need to grade?"""
    total_exams = 120
    monday_grading = 0.6 * total_exams
    remaining_exams = total_exams - monday_grading
    tuesday_grading = 0.75 * remaining_exams
    wednesday_grading = total_exams - monday_grading - tuesday_grading
    result = wednesday_grading
    return result

print(solution())