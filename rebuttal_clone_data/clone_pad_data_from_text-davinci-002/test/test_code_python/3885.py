def solution():
    total_students = 25
    math_students = total_students * (2/5)
    remaining_students = total_students - math_students
    science_students = remaining_students * (1/3)
    history_students = total_students - (math_students + science_students)
    result = history_students + math_students
    
    return result

print(solution())