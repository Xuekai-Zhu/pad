def solution():
    total_students = 180

    # Calculate number of students who bombed finals
    bombed_students = total_students / 4

    # Calculate number of remaining students
    remaining_students = total_students - bombed_students

    # Calculate number of students who didn't show up
    no_show_students = remaining_students / 3

    # Calculate number of students who got less than a D
    fails_students = 20

    # Calculate number of students who passed their finals
    passed_students = total_students - bombed_students - no_show_students - fails_students
    result = passed_students
    return result

print(solution())