def solution():
    
    total_exams = 120
    monday_grading = 0.6 * total_exams
    remaining_exams = total_exams - monday_grading
    tuesday_grading = 0.75 * remaining_exams
    wednesday_grading = total_exams - monday_grading - tuesday_grading
    result = wednesday_grading
    return result

print(solution())