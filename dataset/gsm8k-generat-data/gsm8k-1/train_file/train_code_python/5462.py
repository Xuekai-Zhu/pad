def solution():
    """The fifth grade class at Rosa Parks Elementary School is holding a food drive. Half the students in Ms. Perez's class collected 12 cans each,
    two students didn't collect any, and the remaining 13 students students each collected 4 cans.
    If Ms. Perez's class has 30 students, how many cans did they collect total?"""
    half_students = 15
    half_students_total = half_students * 12
    two_students_total = 0
    remaining_students = 13
    remaining_students_total = remaining_students * 4
    total_students = 30
    total_cans = half_students_total + two_students_total + remaining_students_total
    result = total_cans
    return result

print(solution())