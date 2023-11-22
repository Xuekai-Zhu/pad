def solution():
    
    num_students = 30
    pencils_per_student = 10
    total_pencils = num_students * pencils_per_student
    used_pencils = total_pencils * (1/5)
    remaining_pencils = total_pencils - used_pencils
    left_pencils = remaining_pencils * (1/3)
    result = left_pencils
    return result

print(solution())