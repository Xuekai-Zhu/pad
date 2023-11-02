def solution():
    
    morning_reg = 25
    morning_absent = 3
    afternoon_reg = 24
    afternoon_absent = 4
    total_students = (morning_reg - morning_absent) + (afternoon_reg - afternoon_absent)
    result = total_students
    return result

print(solution())