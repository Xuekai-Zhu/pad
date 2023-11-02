def solution():
    total_students = 28
    absent_fraction = 2/7
    absent_students = total_students * absent_fraction

    # Calculate the number of students present
    present_students = total_students - absent_students
    result = present_students
    return result

print(solution())