def solution():
    
    total_students = 25
    math_students = (2/5) * total_students
    remaining_students = total_students - math_students
    science_students = (1/3) * remaining_students
    history_students = total_students - math_students - science_students
    combined_students = math_students + history_students
    result = combined_students
    return result

print(solution())