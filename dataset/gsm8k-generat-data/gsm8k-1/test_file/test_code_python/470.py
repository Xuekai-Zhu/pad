def solution():
    """At a certain grade level, three-fourths of students have a desktop computer at home. If 20 students do not have desktop computers, how many students are there at that grade level?"""
    students_without_computers = 20
    proportion_with_computers = 3/4
    total_students = (students_without_computers / (1 - proportion_with_computers))
    result = total_students
    return result

print(solution())