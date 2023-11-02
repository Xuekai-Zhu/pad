def solution():
    
    total_students = 50
    free_lunch_students = 0.4 * total_students
    paying_students = total_students - free_lunch_students
    cost_per_paying_student = 210 / paying_students
    result = cost_per_paying_student
    return result

print(solution())