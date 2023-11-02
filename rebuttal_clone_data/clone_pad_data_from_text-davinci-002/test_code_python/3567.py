def solution():
    total_students = 400
    students_invited = total_students * 0.70
    students_not_invited = total_students * 0.30
    students_allowed_in = students_invited - (students_invited * 0.40)
    result = students_allowed_in
    return result

print(solution())