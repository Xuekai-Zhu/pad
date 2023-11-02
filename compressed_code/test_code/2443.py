def solution():
    
    desired_average = 85
    num_students = 10
    current_total = (5 * 92) + (4 * 80)
    needed_total = num_students * desired_average
    last_student_score = needed_total - current_total
    result = last_student_score
    return result

print(solution())