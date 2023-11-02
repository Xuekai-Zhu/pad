def solution():
    total_exams = 120
    exams_graded_monday = total_exams * (60 / 100)
    exams_graded_tuesday = (total_exams - exams_graded_monday) * (75 / 100)
    exams_remaining = total_exams - exams_graded_monday - exams_graded_tuesday
    result = exams_remaining
    return result

print(solution())