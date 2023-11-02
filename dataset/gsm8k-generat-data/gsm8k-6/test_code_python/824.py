def solution():
    # Calculate the total number of classrooms with 30 desks
    classrooms_with_30_desks = 15 // 3 

    # Calculate the total number of classrooms with 25 desks
    classrooms_with_25_desks = 15 - classrooms_with_30_desks 

    # Calculate the total number of students the school can accommodate
    total_students = (classrooms_with_30_desks * 30) + (classrooms_with_25_desks * 25)

    result = total_students
    return result

print(solution())