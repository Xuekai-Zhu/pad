def solution():
    """A school has 15 classrooms. One-third of these classrooms have 30 desks in each classroom and the rest have 25 desks in each classroom. Only one student can sit at one desk. How many students can this school accommodate so that everyone has their own desk?"""
    # Calculate the number of classrooms with 30 desks
    classrooms_30 = 15 // 3

    # Calculate the number of classrooms with 25 desks
    classrooms_25 = 15 - classrooms_30

    # Calculate the total number of desks in the school
    total_desks = (classrooms_30 * 30) + (classrooms_25 * 25)

    # Calculate the maximum number of students that can be accommodated
    max_students = total_desks

    # Display the maximum number of students
    result = max_students
    return result

print(solution())