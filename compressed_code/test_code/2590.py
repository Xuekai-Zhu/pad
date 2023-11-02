def solution():
    
    num_students = 3
    red_pens_per_student = 62
    black_pens_per_student = 43
    total_pens = num_students * (red_pens_per_student + black_pens_per_student)
    total_pens_taken = 37 + 41
    pens_remaining = total_pens - total_pens_taken
    pens_per_student_now = pens_remaining / num_students
    result = pens_per_student_now
    return result

print(solution())