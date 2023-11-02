def solution():
    
    red_pens_per_student = 62
    black_pens_per_student = 43
    total_pens_per_student = red_pens_per_student + black_pens_per_student
    total_students = 3
    total_pens_given = total_pens_per_student * total_students
    pens_taken_first_month = 37
    pens_taken_second_month = 41
    remaining_pens = total_pens_given - pens_taken_first_month - pens_taken_second_month
    pens_per_student_now = remaining_pens / total_students
    result = pens_per_student_now
    return result

print(solution())