def solution():
    # Number of students in each grade
    k = 26
    first = 19
    second = 20
    third = 25

    # Total number of students to check
    total_students = k + first + second + third

    # Time it takes to check each student
    check_time = 2  # 2 minutes per check

    # Total time it will take to complete all the checks
    total_time = (total_students * check_time) / 60  # Convert to hours
    result = total_time
    return result

print(solution())