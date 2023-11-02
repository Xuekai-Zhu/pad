def solution():
    
    total_students = 180
    bombed_students = total_students // 4
    remaining_students = total_students - bombed_students
    skipped_students = remaining_students // 3
    low_grade_students = 20
    passed_students = total_students - (bombed_students + skipped_students + low_grade_students)
    result = passed_students
    return result

print(solution())