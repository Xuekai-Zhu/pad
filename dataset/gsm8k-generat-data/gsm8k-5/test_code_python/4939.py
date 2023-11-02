def solution():
    total_students = 300
    full_scholarship_students = 0.05 * total_students  # 5% of students got full merit scholarship
    half_scholarship_students = 0.1 * total_students  # 10% of students got half merit scholarship
    no_scholarship_students = total_students - full_scholarship_students - half_scholarship_students

    result = no_scholarship_students
    return result

print(solution())