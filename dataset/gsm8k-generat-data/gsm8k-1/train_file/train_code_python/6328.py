def solution():
    """The teachers divided the group of students into 3 groups of 8. But 2 students left early. How many remain?"""
    groups_of_students = 3
    students_per_group = 8
    early_departure = 2
    total_students = groups_of_students * students_per_group
    remaining_students = total_students - early_departure
    result = remaining_students
    return result

print(solution())