def solution():
    """The teachers divided the group of students into 3 groups of 8. But 2 students left early. How many remain?"""
    initial_students = 3 * 8
    students_left = 2
    remaining_students = initial_students - students_left
    result = remaining_students
    return result

print(solution())