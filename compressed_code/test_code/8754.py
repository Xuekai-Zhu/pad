def solution():
    
    total_students = 804
    pass_percent = 75
    pass_students = int(total_students * (pass_percent/100))
    fail_students = total_students - pass_students
    result = fail_students
    return result

print(solution())