def solution():
    total_teachers = 82
    sick_teachers = 13
    substitute_teachers = 9

    # Calculate the number of teachers at school that day
    school_teachers = total_teachers - sick_teachers - substitute_teachers
    result = school_teachers
    return result

print(solution())