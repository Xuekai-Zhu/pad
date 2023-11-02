def solution():
    # Number of classrooms with 30 desks
    num_classrooms_30 = 15 // 3

    # Number of classrooms with 25 desks
    num_classrooms_25 = 15 - num_classrooms_30

    # Total number of desks in classrooms with 30 desks
    total_desks_30 = num_classrooms_30 * 30

    # Total number of desks in classrooms with 25 desks
    total_desks_25 = num_classrooms_25 * 25

    # Total number of students the school can accommodate
    total_students = total_desks_30 + total_desks_25
    result = total_students
    return result

print(solution())