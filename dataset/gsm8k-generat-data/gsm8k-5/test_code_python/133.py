def solution():
    # Calculate the number of students absent
    absent_students = 40 * (1/10)

    # Calculate the number of students present
    present_students = 40 - absent_students

    # Calculate the number of students in the classroom
    classroom_students = present_students * (3/4)

    # Calculate the number of students in the canteen
    canteen_students = present_students - classroom_students
    result = canteen_students
    return result

print(solution())