def solution():
    total_students = 25
    math_students = (2/5) * total_students
    
    remaining_students = total_students - math_students
    science_students = (1/3) * remaining_students
    history_students = remaining_students - science_students
    
    total_likes_math_history = math_students + history_students
    result = total_likes_math_history
    return result

print(solution())