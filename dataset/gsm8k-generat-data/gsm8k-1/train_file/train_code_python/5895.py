def solution():
    """There are 6 girls and 8 boys in the school play. If both parents of each kid attend the premiere, how many parents will be in the auditorium?"""
    total_students = 6 + 8
    parents_per_student = 2
    total_parents = total_students * parents_per_student
    result = total_parents
    return result

print(solution())