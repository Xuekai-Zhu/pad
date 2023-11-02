def solution():
    """A school has 15 classrooms. One-third of these classrooms have 30 desks in each classroom and the rest have 25 desks in each classroom.
    Only one student can sit at one desk. How many students can this school accommodate so that everyone has their own desk?"""
    total_classrooms = 15
    one_third = total_classrooms / 3
    thirty_desks = one_third
    twenty_five_desks = total_classrooms - thirty_desks
    total_desks = (thirty_desks * 30) + (twenty_five_desks * 25)
    total_students = total_desks
    result = total_students
    return result

print(solution())