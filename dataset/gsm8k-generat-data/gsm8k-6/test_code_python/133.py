def solution():
    # Calculate the number of absent students
    absent_students = (1/10) * 40

    # Calculate the number of present students
    present_students = 40 - absent_students

    # Calculate the number of students in the classroom
    classroom_students = (3/4) * present_students

    # Calculate the number of students in the canteen
    canteen_students = present_students - classroom_students
    result = canteen_students
    return result

print(solution())