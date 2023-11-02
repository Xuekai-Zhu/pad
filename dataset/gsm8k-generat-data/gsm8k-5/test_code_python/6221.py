def solution():
    kiah_students = 50  # Number of students from Know It All High School
    karenh_students = (3/5) * kiah_students  # Number of students from Karen High School
    novcor_students = 2 * (kiah_students + karenh_students)  # Number of students from Novel Corona High School

    # Calculate the total number of students at the competition
    total_students = kiah_students + karenh_students + novcor_students
    result = total_students
    return result

print(solution())