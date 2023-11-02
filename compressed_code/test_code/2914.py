def solution():
    
    total_students = 804
    pass_percentage = 75
    fail_percentage = 100 - pass_percentage
    fail_count = (fail_percentage / 100) * total_students
    result = fail_count
    return result

print(solution())