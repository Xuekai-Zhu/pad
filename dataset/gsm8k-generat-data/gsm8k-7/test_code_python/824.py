def solution():
    num_classrooms = 15

    # Calculate the number of classrooms with 30 desks and the number of classrooms with 25 desks
    num_classrooms_30_desks = num_classrooms // 3
    num_classrooms_25_desks = num_classrooms - num_classrooms_30_desks

    # Calculate the total number of desks in all classrooms
    total_desks = (num_classrooms_30_desks * 30) + (num_classrooms_25_desks * 25)

    # Calculate the maximum number of students that can be accommodated with one desk per student
    total_students = total_desks
    result = total_students
    return result

print(solution())