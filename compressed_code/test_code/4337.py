def solution():
    
    total_students = 30
    math_students = total_students // 5
    english_students = total_students // 3
    remaining_students = total_students - math_students - english_students
    science_students = remaining_students // 7
    no_favorite_subject_students = total_students - math_students - english_students - science_students
    result = no_favorite_subject_students
    return result

print(solution())