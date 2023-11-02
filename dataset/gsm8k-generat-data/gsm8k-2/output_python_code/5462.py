def solution():
    """The fifth grade class at Rosa Parks Elementary School is holding a food drive. Half the students in Ms. Perez's class collected 12 cans each, two students didn't collect any, and the remaining 13 students students each collected 4 cans. If Ms. Perez's class has 30 students, how many cans did they collect total?"""
    total_students = 30
    half_students = total_students/2
    cans_per_half = 12
    no_cans_students = 2
    cans_per_remaining = 4
    total_cans = (half_students * cans_per_half) + (total_students - half_students - no_cans_students) * cans_per_remaining
    result = total_cans
    return result

print(solution())