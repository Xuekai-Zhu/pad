def solution():
    """Last Friday, 13 of the 82 teachers at Rydell Elementary School were sick. There were 9 substitute teachers called in to help. How many teachers were at school that day?"""
    total_teachers = 82
    sick_teachers = 13
    substitute_teachers = 9
    present_teachers = total_teachers - sick_teachers + substitute_teachers
    result = present_teachers
    return result

print(solution())