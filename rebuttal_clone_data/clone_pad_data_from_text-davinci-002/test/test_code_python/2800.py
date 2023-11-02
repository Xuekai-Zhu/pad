def solution():
    total_students = 300
    full_merit_students = total_students * 0.05
    half_merit_students = total_students * 0.1
    non_scholarship_students = total_students - (full_merit_students + half_merit_students)
    result = non_scholarship_students
    return result

print(solution())