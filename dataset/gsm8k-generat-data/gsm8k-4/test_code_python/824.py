def solution():
    """A school has 15 classrooms. One-third of these classrooms have 30 desks in each classroom and the rest have 25 desks in each classroom. Only one student can sit at one desk. How many students can this school accommodate so that everyone has their own desk?"""
    # Calculate the number of classrooms with 30 desks
    num_big_classrooms = 15 // 3

    # Calculate the number of desks in the big classrooms
    big_classroom_desks = num_big_classrooms * 30

    # Calculate the number of classrooms with 25 desks
    num_small_classrooms = 15 - num_big_classrooms

    # Calculate the number of desks in the small classrooms
    small_classroom_desks = num_small_classrooms * 25

    # Calculate the total number of desks
    total_desks = big_classroom_desks + small_classroom_desks

    # Calculate the number of students that can be accommodated
    num_students = total_desks

    result = num_students
    return result

print(solution())