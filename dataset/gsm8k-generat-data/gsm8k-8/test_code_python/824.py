def solution():
    # Calculate the number of classrooms with 30 desks
    num_30_desks = 15 // 3

    # Calculate the number of classrooms with 25 desks
    num_25_desks = 15 - num_30_desks

    # Calculate the total number of desks
    total_desks = num_30_desks * 30 + num_25_desks * 25

    # Calculate the total number of students
    total_students = total_desks

    result = total_students
    return result

print(solution())