def solution():
    boys_in_second = 20
    girls_in_second = 11

    # Total number of students in second grade
    total_second = boys_in_second + girls_in_second

    # Total number of students in third grade
    total_third = 2 * total_second

    # Total number of students in grades 2 and 3
    total_students = total_second + total_third
    result = total_students
    return result

print(solution())