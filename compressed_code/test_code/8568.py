def solution():
    
    total_contribution = 90
    class_funds = 14
    remaining_contribution = total_contribution - class_funds
    num_students = 19
    contribution_per_student = remaining_contribution / num_students
    result = contribution_per_student
    return result

print(solution())