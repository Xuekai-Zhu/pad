def solution():
    
    total_contribution = 90
    class_funds = 14
    remaining_amount = total_contribution - class_funds
    num_students = 19
    per_student_contribution = remaining_amount / num_students
    result = per_student_contribution
    return result

print(solution())