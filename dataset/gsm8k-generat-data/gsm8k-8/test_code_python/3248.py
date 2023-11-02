def solution():
    # Calculate the number of students who bombed their finals
    bombed_students = 180 * (1/4)

    # Calculate the number of students who didn't show up
    no_show_students = (180 - bombed_students) * (1/3)

    # Calculate the number of students who got less than a D
    less_than_D_students = 20

    # Calculate the number of students who passed their finals
    passed_students = 180 - bombed_students - no_show_students - less_than_D_students
    result = passed_students
    return result

print(solution())